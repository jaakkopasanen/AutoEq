# Sennheiser CX 880
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.5dB
GraphicEQ: 21 -4.6; 23 -5.1; 25 -5.4; 28 -5.9; 31 -6.3; 34 -6.6; 37 -6.9; 41 -7.2; 45 -7.5; 49 -7.7; 54 -7.9; 60 -8.2; 66 -8.5; 72 -8.8; 79 -8.9; 87 -9.1; 96 -9.2; 106 -9.2; 116 -9.2; 128 -9.2; 141 -9.0; 155 -8.9; 170 -8.7; 187 -8.3; 206 -7.9; 227 -7.4; 249 -6.9; 274 -6.4; 302 -5.7; 332 -5.0; 365 -4.2; 402 -3.5; 442 -3.1; 486 -2.5; 535 -1.8; 588 -1.2; 647 -0.6; 712 -0.0; 783 0.2; 861 0.3; 947 0.2; 1042 -0.1; 1146 -0.3; 1261 -0.9; 1387 -1.1; 1526 -1.9; 1678 -2.2; 1846 -2.2; 2031 -2.0; 2234 -1.6; 2457 -0.9; 2703 -0.1; 2973 1.1; 3270 2.7; 3597 3.4; 3957 2.0; 4353 -0.8; 4788 -2.8; 5267 -4.5; 5793 -6.5; 6373 -6.4; 7010 -4.9; 7711 -5.6; 8482 -9.1; 9330 -10.4; 10263 -4.8; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser CX 880 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-35**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser CX 880 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 47 Hz    | 0.38 | -6.3 dB  |
| Peaking | 133 Hz   | 0.69 | -5.1 dB  |
| Peaking | 263 Hz   | 1.12 | -3.0 dB  |
| Peaking | 6015 Hz  | 3.66 | -6.5 dB  |
| Peaking | 8995 Hz  | 3.89 | -11.1 dB |
| Peaking | 855 Hz   | 2.08 | 1.4 dB   |
| Peaking | 1894 Hz  | 1.42 | -2.5 dB  |
| Peaking | 3628 Hz  | 2.5  | 5.5 dB   |
| Peaking | 4614 Hz  | 2.54 | -2.5 dB  |
| Peaking | 11333 Hz | 5.96 | 2.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20CX%20880/Sennheiser%20CX%20880.png)