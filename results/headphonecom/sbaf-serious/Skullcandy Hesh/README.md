# Skullcandy Hesh
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 5.8; 72 4.8; 79 2.9; 87 1.3; 96 0.3; 106 -0.2; 116 -0.4; 128 -0.4; 141 -0.6; 155 -0.5; 170 -0.4; 187 -0.6; 206 -0.6; 227 -0.3; 249 -0.1; 274 0.1; 302 0.3; 332 0.3; 365 0.2; 402 0.1; 442 -0.1; 486 -0.4; 535 -0.6; 588 -1.0; 647 -0.9; 712 -0.3; 783 0.5; 861 0.3; 947 0.6; 1042 -1.0; 1146 -3.2; 1261 -5.3; 1387 -4.9; 1526 -5.4; 1678 -2.7; 1846 0.1; 2031 3.2; 2234 5.8; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Hesh GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Hesh ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 50 Hz   | 0.38 | 8.2 dB   |
| Peaking | 115 Hz  | 0.79 | -5.9 dB  |
| Peaking | 584 Hz  | 3.61 | -1.6 dB  |
| Peaking | 1452 Hz | 1.88 | -11.0 dB |
| Peaking | 2746 Hz | 0.56 | 8.2 dB   |
| Peaking | 66 Hz   | 6.87 | 1.2 dB   |
| Peaking | 939 Hz  | 8.79 | 1.2 dB   |
| Peaking | 3268 Hz | 4.34 | -1.0 dB  |
| Peaking | 6266 Hz | 1.95 | 6.3 dB   |
| Peaking | 7383 Hz | 1.41 | -5.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Skullcandy%20Hesh/Skullcandy%20Hesh.png)