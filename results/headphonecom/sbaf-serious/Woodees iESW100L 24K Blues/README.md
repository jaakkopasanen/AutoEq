# Woodees iESW100L 24K Blues
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.0dB
GraphicEQ: 21 -10.5; 23 -10.6; 25 -10.6; 28 -10.5; 31 -10.5; 34 -10.5; 37 -10.4; 41 -10.4; 45 -10.4; 49 -10.5; 54 -10.5; 60 -10.5; 66 -10.6; 72 -10.7; 79 -10.7; 87 -10.7; 96 -10.6; 106 -10.5; 116 -10.3; 128 -10.2; 141 -9.9; 155 -9.7; 170 -9.4; 187 -8.9; 206 -8.4; 227 -7.9; 249 -7.3; 274 -6.7; 302 -6.0; 332 -5.2; 365 -4.5; 402 -3.7; 442 -3.1; 486 -2.5; 535 -1.8; 588 -1.1; 647 -0.5; 712 0.0; 783 0.3; 861 0.3; 947 0.2; 1042 0.0; 1146 -0.2; 1261 -0.7; 1387 -1.7; 1526 -2.5; 1678 -3.2; 1846 -3.5; 2031 -3.9; 2234 -4.3; 2457 -4.5; 2703 -4.5; 2973 -2.9; 3270 -0.3; 3597 1.5; 3957 0.2; 4353 -3.2; 4788 -7.7; 5267 -10.9; 5793 -3.1; 6373 1.7; 7010 2.4; 7711 0.3; 8482 -1.8; 9330 -5.0; 10263 -1.1; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Woodees iESW100L 24K Blues GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-30**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Woodees iESW100L 24K Blues ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 64 Hz    | 0.12 | -11.1 dB |
| Peaking | 1935 Hz  | 0.21 | 7.7 dB   |
| Peaking | 2149 Hz  | 0.87 | -11.5 dB |
| Peaking | 5116 Hz  | 5.04 | -14.8 dB |
| Peaking | 9401 Hz  | 4.17 | -7.5 dB  |
| Peaking | 2811 Hz  | 5.96 | -2.2 dB  |
| Peaking | 3725 Hz  | 3.36 | 3.6 dB   |
| Peaking | 4310 Hz  | 3.06 | -2.6 dB  |
| Peaking | 6668 Hz  | 8.28 | 2.6 dB   |
| Peaking | 14334 Hz | 1.42 | -0.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Woodees%20iESW100L%2024K%20Blues/Woodees%20iESW100L%2024K%20Blues.png)