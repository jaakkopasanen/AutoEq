# Bose QuietComfort 15
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.9dB
GraphicEQ: 21 -7.0; 23 -9.0; 25 -10.3; 28 -10.8; 31 -10.0; 34 -8.8; 37 -7.9; 41 -7.3; 45 -6.9; 49 -6.6; 54 -6.3; 60 -6.0; 66 -6.0; 72 -6.2; 79 -6.3; 87 -6.2; 96 -6.2; 106 -6.0; 116 -5.8; 128 -5.7; 141 -5.6; 155 -5.3; 170 -5.0; 187 -4.9; 206 -4.7; 227 -4.4; 249 -4.4; 274 -4.1; 302 -3.8; 332 -3.4; 365 -2.9; 402 -2.5; 442 -2.2; 486 -1.8; 535 -1.4; 588 -0.9; 647 -0.2; 712 -0.1; 783 0.5; 861 0.8; 947 0.4; 1042 -0.2; 1146 -0.9; 1261 -1.7; 1387 -2.1; 1526 -2.1; 1678 -4.0; 1846 -6.3; 2031 -8.6; 2234 -9.8; 2457 -9.3; 2703 -7.2; 2973 -4.3; 3270 -2.6; 3597 -2.8; 3957 -7.0; 4353 -10.2; 4788 -6.8; 5267 -3.6; 5793 -6.8; 6373 -3.4; 7010 -2.2; 7711 0.1; 8482 -0.8; 9330 -5.3; 10263 -6.6; 11289 -3.6; 12418 -1.6; 13660 -1.2; 15026 -1.3; 16529 -2.3; 18182 -5.0; 20000 -8.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietComfort 15 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-8**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 15 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 27 Hz    | 1.23 | -9.0 dB  |
| Peaking | 114 Hz   | 0.41 | -5.6 dB  |
| Peaking | 2241 Hz  | 2.56 | -10.1 dB |
| Peaking | 4466 Hz  | 3.13 | -8.7 dB  |
| Peaking | 10180 Hz | 3.17 | -6.5 dB  |
| Peaking | 311 Hz   | 2.32 | -0.8 dB  |
| Peaking | 839 Hz   | 2.59 | 1.9 dB   |
| Peaking | 3413 Hz  | 5.53 | 2.4 dB   |
| Peaking | 12723 Hz | 0.45 | 8.9 dB   |
| Peaking | 20718 Hz | 0.1  | -10.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Bose%20QuietComfort%2015/Bose%20QuietComfort%2015.png)