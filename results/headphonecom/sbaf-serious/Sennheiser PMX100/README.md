# Sennheiser PMX100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.6; 25 1.0; 28 0.2; 31 -0.4; 34 -0.9; 37 -1.3; 41 -1.8; 45 -2.1; 49 -2.5; 54 -2.9; 60 -3.3; 66 -3.6; 72 -3.9; 79 -4.2; 87 -4.6; 96 -4.8; 106 -4.9; 116 -4.9; 128 -5.1; 141 -5.2; 155 -5.1; 170 -4.9; 187 -4.6; 206 -4.5; 227 -4.2; 249 -3.6; 274 -3.1; 302 -2.7; 332 -2.2; 365 -1.9; 402 -1.6; 442 -1.3; 486 -1.0; 535 -0.6; 588 -0.4; 647 -0.2; 712 0.0; 783 0.2; 861 0.2; 947 0.1; 1042 -0.1; 1146 -0.2; 1261 -0.6; 1387 -1.3; 1526 -2.3; 1678 -3.0; 1846 -3.4; 2031 -3.2; 2234 -1.5; 2457 0.2; 2703 1.9; 2973 4.9; 3270 6.0; 3597 6.0; 3957 0.2; 4353 -7.2; 4788 -2.7; 5267 3.3; 5793 5.9; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PMX100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PMX100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 129 Hz  | 0.56 | -5.4 dB  |
| Peaking | 1916 Hz | 2.35 | -4.7 dB  |
| Peaking | 3490 Hz | 2.18 | 9.5 dB   |
| Peaking | 4366 Hz | 4.42 | -13.3 dB |
| Peaking | 5840 Hz | 3.5  | 7.2 dB   |
| Peaking | 16 Hz   | 1.33 | 3.6 dB   |
| Peaking | 45 Hz   | 1.62 | -0.7 dB  |
| Peaking | 229 Hz  | 4.06 | -0.5 dB  |
| Peaking | 775 Hz  | 1.98 | 0.8 dB   |
| Peaking | 8283 Hz | 4.75 | -1.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20PMX100/Sennheiser%20PMX100.png)