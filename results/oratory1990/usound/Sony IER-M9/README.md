# Sony IER-M9

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.5dB
GraphicEQ: 21 -1.8; 23 -2.0; 25 -2.1; 28 -2.2; 31 -2.4; 34 -2.5; 37 -2.6; 41 -2.7; 45 -2.8; 49 -2.8; 54 -3.0; 60 -3.2; 66 -3.3; 72 -3.5; 79 -3.7; 87 -3.8; 96 -4.0; 106 -4.1; 116 -4.3; 128 -4.3; 141 -4.3; 155 -4.3; 170 -4.2; 187 -4.0; 206 -3.8; 227 -3.5; 249 -3.3; 274 -3.0; 302 -2.8; 332 -2.6; 365 -2.3; 402 -2.1; 442 -1.8; 486 -1.6; 535 -1.2; 588 -0.9; 647 -0.6; 712 -0.3; 783 -0.1; 861 0.1; 947 0.1; 1042 -0.1; 1146 -0.5; 1261 -0.7; 1387 -0.8; 1526 -0.6; 1678 -0.2; 1846 0.2; 2031 0.8; 2234 1.4; 2457 2.4; 2703 3.0; 2973 1.5; 3270 -0.9; 3597 -0.9; 3957 0.7; 4353 0.7; 4788 0.9; 5267 2.8; 5793 4.2; 6373 4.2; 7010 2.4; 7711 0.2; 8482 -1.9; 9330 -3.8; 10263 -6.0; 11289 -6.9; 12418 -4.7; 13660 -3.4; 15026 -6.2; 16529 -8.4; 18182 -5.2; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony IER-M9 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-44**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony IER-M9 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 44 Hz    |  0.29 | -2.0 dB |
| Peaking | 168 Hz   |  0.53 | -3.3 dB |
| Peaking | 6163 Hz  |  2.47 | 5.4 dB  |
| Peaking | 10726 Hz |  2.12 | -6.6 dB |
| Peaking | 16613 Hz |  1.86 | -8.6 dB |
| Peaking | 862 Hz   |  1.76 | 1.5 dB  |
| Peaking | 1611 Hz  |  0.46 | -1.3 dB |
| Peaking | 2706 Hz  |  1.88 | 4.4 dB  |
| Peaking | 3343 Hz  |  4.84 | -3.4 dB |
| Peaking | 13426 Hz | 10.04 | 1.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Sony%20IER-M9/Sony%20IER-M9.png)