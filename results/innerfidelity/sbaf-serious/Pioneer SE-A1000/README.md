# Pioneer SE-A1000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 5.9; 66 4.5; 72 2.9; 79 1.5; 87 0.3; 96 -0.6; 106 -1.1; 116 -1.4; 128 -1.8; 141 -1.9; 155 -1.9; 170 -1.7; 187 -1.7; 206 -1.5; 227 -1.2; 249 -1.0; 274 -0.7; 302 -0.7; 332 -0.6; 365 -0.1; 402 0.0; 442 0.3; 486 0.8; 535 1.2; 588 1.1; 647 0.9; 712 0.6; 783 0.7; 861 0.2; 947 0.1; 1042 -0.2; 1146 -0.3; 1261 -0.1; 1387 0.1; 1526 0.3; 1678 0.8; 1846 1.7; 2031 2.7; 2234 2.9; 2457 3.0; 2703 2.0; 2973 1.3; 3270 1.6; 3597 2.3; 3957 -3.5; 4353 -8.2; 4788 -6.9; 5267 -3.7; 5793 -1.8; 6373 0.1; 7010 1.5; 7711 -1.8; 8482 -4.3; 9330 -5.5; 10263 -4.8; 11289 -1.1; 12418 0.0; 13660 -0.3; 15026 -0.5; 16529 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Pioneer SE-A1000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pioneer SE-A1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 35 Hz   | 1.03 | 7.3 dB   |
| Peaking | 3667 Hz | 1.07 | 6.9 dB   |
| Peaking | 4431 Hz | 2.6  | -14.2 dB |
| Peaking | 6781 Hz | 7.64 | 3.9 dB   |
| Peaking | 9341 Hz | 2.78 | -6.2 dB  |
| Peaking | 60 Hz   | 2.55 | 4.1 dB   |
| Peaking | 127 Hz  | 0.64 | -2.6 dB  |
| Peaking | 577 Hz  | 1.59 | 1.6 dB   |
| Peaking | 1573 Hz | 0.74 | -1.0 dB  |
| Peaking | 2097 Hz | 3.27 | 2.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Pioneer%20SE-A1000/Pioneer%20SE-A1000.png)