# Sony MDR-1RBT
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 0.4; 25 -0.5; 28 -1.6; 31 -2.6; 34 -3.4; 37 -4.1; 41 -4.9; 45 -5.6; 49 -6.2; 54 -6.7; 60 -7.2; 66 -7.8; 72 -8.4; 79 -8.7; 87 -9.4; 96 -9.2; 106 -8.4; 116 -7.6; 128 -7.6; 141 -7.8; 155 -7.8; 170 -4.1; 187 -4.0; 206 -1.8; 227 0.9; 249 4.1; 274 5.0; 302 6.0; 332 5.5; 365 5.0; 402 3.4; 442 1.5; 486 0.8; 535 1.8; 588 3.0; 647 2.1; 712 1.1; 783 2.4; 861 1.2; 947 0.0; 1042 0.3; 1146 0.6; 1261 -1.0; 1387 -3.1; 1526 -5.5; 1678 -6.9; 1846 -8.6; 2031 -8.3; 2234 -8.3; 2457 -5.0; 2703 -1.6; 2973 1.3; 3270 1.5; 3597 -0.2; 3957 -1.1; 4353 0.4; 4788 3.9; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -2.9; 9330 -4.8; 10263 -0.3; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-1RBT GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-1RBT ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 75 Hz   | 1.24 | -9.5 dB  |
| Peaking | 139 Hz  | 3.35 | -6.0 dB  |
| Peaking | 1955 Hz | 2.75 | -10.1 dB |
| Peaking | 5621 Hz | 3.3  | 7.3 dB   |
| Peaking | 309 Hz  | 2.61 | 7.2 dB   |
| Peaking | 671 Hz  | 1.8  | 2.2 dB   |
| Peaking | 6582 Hz | 7.52 | 2.2 dB   |
| Peaking | 9053 Hz | 5.56 | -5.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-1RBT/Sony%20MDR-1RBT.png)