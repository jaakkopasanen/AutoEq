# Sennheiser HD 380 Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.6dB
GraphicEQ: 21 -9.7; 23 -9.8; 25 -9.9; 28 -9.9; 31 -9.9; 34 -9.8; 37 -9.7; 41 -9.4; 45 -9.1; 49 -8.6; 54 -7.9; 60 -7.1; 66 -6.0; 72 -5.2; 79 -3.4; 87 -0.8; 96 1.0; 106 -2.0; 116 -3.2; 128 -2.8; 141 -4.6; 155 -2.8; 170 -1.3; 187 -1.3; 206 0.5; 227 1.6; 249 1.8; 274 1.5; 302 0.7; 332 -0.5; 365 -1.4; 402 -2.0; 442 -2.2; 486 -2.4; 535 -2.3; 588 -1.7; 647 -1.2; 712 -1.0; 783 -0.5; 861 -0.3; 947 -0.2; 1042 0.1; 1146 0.3; 1261 0.4; 1387 0.4; 1526 0.0; 1678 -0.8; 1846 -2.9; 2031 -4.2; 2234 -4.2; 2457 -3.9; 2703 -1.8; 2973 0.6; 3270 2.0; 3597 -0.3; 3957 -1.9; 4353 -2.6; 4788 0.6; 5267 4.1; 5793 3.9; 6373 2.7; 7010 0.7; 7711 0.3; 8482 0.0; 9330 -0.2; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.0; 20000 -0.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 380 Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-45**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 380 Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.65 | -9.8 dB |
| Peaking | 52 Hz   | 1.92 | -3.5 dB |
| Peaking | 493 Hz  | 2.8  | -2.6 dB |
| Peaking | 2179 Hz | 3.53 | -5.0 dB |
| Peaking | 5654 Hz | 5.2  | 5.0 dB  |
| Peaking | 93 Hz   | 4.53 | 5.7 dB  |
| Peaking | 131 Hz  | 0.93 | -3.3 dB |
| Peaking | 237 Hz  | 2.4  | 3.8 dB  |
| Peaking | 3238 Hz | 7.83 | 3.0 dB  |
| Peaking | 4185 Hz | 6.54 | -3.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20380%20Pro/Sennheiser%20HD%20380%20Pro.png)