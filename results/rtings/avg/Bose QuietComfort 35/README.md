# Bose QuietComfort 35

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.6dB
GraphicEQ: 21 -6.0; 23 -5.5; 25 -5.2; 28 -5.0; 31 -5.0; 34 -5.0; 37 -5.1; 41 -5.2; 45 -5.3; 49 -5.3; 54 -5.2; 60 -5.1; 66 -5.1; 72 -5.1; 79 -5.0; 87 -5.0; 96 -4.9; 106 -4.9; 116 -4.9; 128 -4.8; 141 -4.7; 155 -4.6; 170 -4.5; 187 -4.3; 206 -4.1; 227 -3.9; 249 -3.7; 274 -3.5; 302 -3.4; 332 -3.2; 365 -3.0; 402 -2.9; 442 -2.8; 486 -2.7; 535 -2.5; 588 -2.1; 647 -1.7; 712 -1.3; 783 -0.9; 861 -0.4; 947 -0.2; 1042 0.1; 1146 0.2; 1261 -0.3; 1387 -1.9; 1526 -3.5; 1678 -5.6; 1846 -7.7; 2031 -8.0; 2234 -6.1; 2457 -4.9; 2703 -5.9; 2973 -5.9; 3270 -4.4; 3597 -4.6; 3957 -5.7; 4353 -4.5; 4788 -2.5; 5267 0.4; 5793 -4.6; 6373 -8.5; 7010 -3.4; 7711 0.2; 8482 0.0; 9330 0.0; 10263 0.0; 11289 -2.3; 12418 -7.6; 13660 -7.7; 15026 -6.7; 16529 -4.5; 18182 -2.9; 20000 -4.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietComfort 35 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-5**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 35 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 33 Hz    | 0.09 | -5.3 dB  |
| Peaking | 1934 Hz  | 3.52 | -6.5 dB  |
| Peaking | 3527 Hz  | 0.96 | -4.8 dB  |
| Peaking | 13022 Hz | 3.99 | -6.1 dB  |
| Peaking | 15751 Hz | 1.45 | -5.4 dB  |
| Peaking | 1082 Hz  | 2.41 | 2.7 dB   |
| Peaking | 5324 Hz  | 6.72 | 5.1 dB   |
| Peaking | 6332 Hz  | 4.41 | -10.0 dB |
| Peaking | 7661 Hz  | 1.24 | 4.1 dB   |
| Peaking | 17419 Hz | 0.01 | -0.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bose%20QuietComfort%2035/Bose%20QuietComfort%2035.png)