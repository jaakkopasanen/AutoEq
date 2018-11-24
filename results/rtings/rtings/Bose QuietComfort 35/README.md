# Bose QuietComfort 35

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.2dB
GraphicEQ: 21 -6.0; 23 -5.5; 25 -5.2; 28 -5.0; 31 -5.0; 34 -5.0; 37 -5.1; 41 -5.2; 45 -5.3; 49 -5.3; 54 -5.2; 60 -5.1; 66 -5.1; 72 -5.1; 79 -5.0; 87 -5.0; 96 -4.9; 106 -4.9; 116 -4.9; 128 -4.8; 141 -4.7; 155 -4.6; 170 -4.5; 187 -4.3; 206 -4.1; 227 -3.9; 249 -3.7; 274 -3.5; 302 -3.4; 332 -3.2; 365 -3.0; 402 -2.9; 442 -2.8; 486 -2.7; 535 -2.5; 588 -2.1; 647 -1.7; 712 -1.3; 783 -0.9; 861 -0.4; 947 -0.2; 1042 0.1; 1146 0.2; 1261 -0.3; 1387 -1.9; 1526 -3.5; 1678 -5.6; 1846 -7.7; 2031 -8.0; 2234 -6.1; 2457 -4.9; 2703 -5.7; 2973 -5.4; 3270 -3.7; 3597 -3.6; 3957 -4.4; 4353 -3.2; 4788 -0.8; 5267 3.0; 5793 -2.1; 6373 -7.2; 7010 -2.8; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 -1.5; 12418 -4.3; 13660 -4.4; 15026 -4.1; 16529 -1.5; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietComfort 35 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-31**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 35 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 37 Hz    | 0.15 | -5.4 dB |
| Peaking | 325 Hz   | 1.03 | -1.3 dB |
| Peaking | 2208 Hz  | 1.43 | -7.3 dB |
| Peaking | 6410 Hz  | 9.55 | -7.5 dB |
| Peaking | 13903 Hz | 2.27 | -5.1 dB |
| Peaking | 1204 Hz  | 2.1  | 3.2 dB  |
| Peaking | 2047 Hz  | 1.33 | -3.4 dB |
| Peaking | 2337 Hz  | 4.62 | 5.0 dB  |
| Peaking | 4047 Hz  | 5.58 | -2.4 dB |
| Peaking | 5293 Hz  | 9.42 | 5.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Bose%20QuietComfort%2035/Bose%20QuietComfort%2035.png)