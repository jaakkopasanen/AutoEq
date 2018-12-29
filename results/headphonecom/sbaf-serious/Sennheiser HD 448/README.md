# Sennheiser HD 448
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 5.5; 116 4.6; 128 3.6; 141 2.0; 155 -0.1; 170 -0.4; 187 0.6; 206 2.3; 227 3.6; 249 2.1; 274 1.9; 302 2.6; 332 2.0; 365 2.0; 402 2.4; 442 2.3; 486 2.5; 535 1.8; 588 1.5; 647 1.2; 712 0.3; 783 -0.2; 861 0.1; 947 0.6; 1042 -0.1; 1146 0.2; 1261 -0.9; 1387 -0.7; 1526 -1.3; 1678 -1.6; 1846 -2.2; 2031 -2.5; 2234 -0.8; 2457 1.1; 2703 0.8; 2973 1.3; 3270 1.6; 3597 1.5; 3957 2.7; 4353 6.0; 4788 6.0; 5267 2.9; 5793 3.2; 6373 5.3; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 448 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 448 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 0.51 | 6.3 dB  |
| Peaking | 91 Hz    | 1.87 | 3.9 dB  |
| Peaking | 379 Hz   | 1.32 | 2.3 dB  |
| Peaking | 4798 Hz  | 2.09 | 5.7 dB  |
| Peaking | 24000 Hz | 2.44 | 2.1 dB  |
| Peaking | 125 Hz   | 3.28 | 1.3 dB  |
| Peaking | 164 Hz   | 3.27 | -2.9 dB |
| Peaking | 219 Hz   | 5.73 | 2.6 dB  |
| Peaking | 2045 Hz  | 2.13 | -4.1 dB |
| Peaking | 2350 Hz  | 2.58 | 2.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20448/Sennheiser%20HD%20448.png)