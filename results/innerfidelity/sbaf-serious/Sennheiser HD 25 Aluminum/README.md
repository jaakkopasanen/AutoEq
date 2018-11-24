# Sennheiser HD 25 Aluminum

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -3.5; 23 -3.8; 25 -4.0; 28 -4.3; 31 -4.5; 34 -4.6; 37 -4.7; 41 -4.8; 45 -4.8; 49 -4.8; 54 -4.8; 60 -4.7; 66 -4.7; 72 -4.6; 79 -4.1; 87 -4.0; 96 -5.3; 106 -6.6; 116 -7.2; 128 -7.2; 141 -6.7; 155 -5.8; 170 -5.4; 187 -4.6; 206 -3.6; 227 -2.6; 249 -1.4; 274 0.1; 302 1.0; 332 1.7; 365 2.2; 402 2.5; 442 2.6; 486 2.0; 535 1.7; 588 1.7; 647 1.4; 712 1.0; 783 1.0; 861 0.5; 947 0.1; 1042 -0.2; 1146 -0.4; 1261 -0.9; 1387 -1.8; 1526 -2.8; 1678 -3.8; 1846 -4.3; 2031 -4.5; 2234 -3.8; 2457 -2.4; 2703 -0.9; 2973 0.4; 3270 0.8; 3597 0.4; 3957 0.5; 4353 2.1; 4788 5.6; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 -1.9; 8482 -6.3; 9330 -5.0; 10263 -0.2; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 25 Aluminum GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 25 Aluminum ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 39 Hz   | 0.62 | -4.9 dB |
| Peaking | 131 Hz  | 1.69 | -6.6 dB |
| Peaking | 1958 Hz | 2.3  | -5.3 dB |
| Peaking | 5782 Hz | 1.82 | 7.4 dB  |
| Peaking | 8592 Hz | 3.92 | -9.0 dB |
| Peaking | 140 Hz  | 3.48 | 1.8 dB  |
| Peaking | 205 Hz  | 1.05 | -3.9 dB |
| Peaking | 347 Hz  | 0.8  | 4.3 dB  |
| Peaking | 1068 Hz | 2.46 | -0.2 dB |
| Peaking | 1510 Hz | 4.43 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%2025%20Aluminum/Sennheiser%20HD%2025%20Aluminum.png)