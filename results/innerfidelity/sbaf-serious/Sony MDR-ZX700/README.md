# Sony MDR-ZX700

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 5.8; 49 4.8; 54 3.2; 60 1.4; 66 0.1; 72 -0.7; 79 -1.4; 87 -1.7; 96 -2.5; 106 -2.9; 116 -2.8; 128 -3.6; 141 -3.9; 155 -3.7; 170 -2.4; 187 -3.2; 206 -3.4; 227 -3.2; 249 -3.2; 274 -2.9; 302 -2.7; 332 -3.7; 365 -2.7; 402 -2.3; 442 -1.9; 486 -1.7; 535 -1.2; 588 -0.3; 647 0.3; 712 0.5; 783 0.7; 861 0.7; 947 0.3; 1042 -0.2; 1146 -0.7; 1261 -1.2; 1387 -2.6; 1526 -4.2; 1678 -6.1; 1846 -7.5; 2031 -7.3; 2234 -5.6; 2457 -3.6; 2703 -2.3; 2973 -0.9; 3270 0.3; 3597 2.7; 3957 6.0; 4353 6.0; 4788 6.0; 5267 4.8; 5793 3.6; 6373 5.4; 7010 2.5; 7711 -1.5; 8482 -8.9; 9330 -10.3; 10263 -3.3; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-ZX700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-ZX700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.6dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 31 Hz   | 1.65 | 7.5 dB   |
| Peaking | 1959 Hz | 1.98 | -8.3 dB  |
| Peaking | 4373 Hz | 2.25 | 7.1 dB   |
| Peaking | 6529 Hz | 3.44 | 5.2 dB   |
| Peaking | 8931 Hz | 4.19 | -13.0 dB |
| Peaking | 21 Hz   | 2.88 | 3.8 dB   |
| Peaking | 48 Hz   | 3.58 | 3.6 dB   |
| Peaking | 123 Hz  | 0.99 | -3.6 dB  |
| Peaking | 229 Hz  | 2.33 | -1.7 dB  |
| Peaking | 348 Hz  | 2.75 | -2.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-ZX700/Sony%20MDR-ZX700.png)