# Sennheiser HD 800

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.7dB
GraphicEQ: 21 0.0; 23 3.1; 25 2.8; 28 2.4; 31 2.1; 34 1.9; 37 1.7; 41 1.6; 45 1.6; 49 1.6; 54 1.9; 60 1.8; 66 1.1; 72 0.2; 79 -0.4; 87 -0.9; 96 -1.4; 106 -1.7; 116 -1.8; 128 -2.2; 141 -2.4; 155 -2.6; 170 -2.7; 187 -2.8; 206 -2.9; 227 -2.8; 249 -2.9; 274 -2.7; 302 -2.6; 332 -2.5; 365 -2.3; 402 -2.2; 442 -1.8; 486 -1.8; 535 -1.6; 588 -1.2; 647 -1.1; 712 -1.1; 783 -0.5; 861 -0.5; 947 -0.1; 1042 0.3; 1146 0.7; 1261 1.4; 1387 1.5; 1526 1.6; 1678 1.3; 1846 1.1; 2031 1.6; 2234 1.4; 2457 2.1; 2703 2.5; 2973 2.0; 3270 2.2; 3597 1.3; 3957 -0.2; 4353 -2.2; 4788 -2.6; 5267 -3.2; 5793 -4.0; 6373 -5.0; 7010 -3.6; 7711 -1.4; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -0.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 800 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-36**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 800 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 17 Hz    | 0.59 | 3.7 dB  |
| Peaking | 59 Hz    | 2.09 | 2.2 dB  |
| Peaking | 216 Hz   | 0.38 | -3.0 dB |
| Peaking | 4015 Hz  | 0.42 | 4.1 dB  |
| Peaking | 5743 Hz  | 1.27 | -8.3 dB |
| Peaking | 1972 Hz  | 2.34 | -2.1 dB |
| Peaking | 1977 Hz  | 1.3  | 1.4 dB  |
| Peaking | 6773 Hz  | 6.97 | -1.3 dB |
| Peaking | 8316 Hz  | 3.8  | 1.2 dB  |
| Peaking | 13391 Hz | 0.83 | -0.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20800/Sennheiser%20HD%20800.png)