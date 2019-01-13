# Sony MDR-ZX1000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 5.6; 66 4.6; 72 3.7; 79 2.9; 87 2.2; 96 1.8; 106 1.5; 116 1.0; 128 0.3; 141 -0.2; 155 -0.1; 170 0.8; 187 1.0; 206 1.3; 227 1.7; 249 1.8; 274 1.7; 302 1.4; 332 0.5; 365 -0.2; 402 -0.5; 442 -0.6; 486 -0.7; 535 -0.6; 588 -0.2; 647 0.1; 712 -0.1; 783 0.1; 861 0.1; 947 -0.0; 1042 -0.0; 1146 -0.3; 1261 -0.7; 1387 -1.8; 1526 -3.1; 1678 -4.3; 1846 -4.8; 2031 -4.6; 2234 -3.8; 2457 -2.6; 2703 -1.3; 2973 0.2; 3270 1.8; 3597 4.7; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 5.5; 6373 5.5; 7010 2.5; 7711 -0.3; 8482 -5.3; 9330 -6.9; 10263 -2.9; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-ZX1000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-ZX1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 35 Hz   | 0.66 | 6.8 dB   |
| Peaking | 254 Hz  | 3.79 | 1.8 dB   |
| Peaking | 2110 Hz | 1.36 | -7.6 dB  |
| Peaking | 4935 Hz | 0.71 | 8.2 dB   |
| Peaking | 8992 Hz | 2.86 | -11.1 dB |
| Peaking | 60 Hz   | 4.69 | 1.3 dB   |
| Peaking | 137 Hz  | 4.14 | -1.4 dB  |
| Peaking | 469 Hz  | 2.99 | -1.0 dB  |
| Peaking | 1153 Hz | 1.13 | 0.8 dB   |
| Peaking | 1625 Hz | 4.35 | -1.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-ZX1000/Sony%20MDR-ZX1000.png)