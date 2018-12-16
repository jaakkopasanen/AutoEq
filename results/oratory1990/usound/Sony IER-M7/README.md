# Sony IER-M7

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 21 -1.1; 23 -1.2; 25 -1.4; 28 -1.5; 31 -1.6; 34 -1.7; 37 -1.8; 41 -1.9; 45 -2.0; 49 -2.1; 54 -2.2; 60 -2.4; 66 -2.5; 72 -2.7; 79 -2.9; 87 -3.1; 96 -3.3; 106 -3.4; 116 -3.6; 128 -3.6; 141 -3.7; 155 -3.7; 170 -3.6; 187 -3.5; 206 -3.3; 227 -3.2; 249 -3.0; 274 -2.7; 302 -2.5; 332 -2.3; 365 -2.1; 402 -1.9; 442 -1.7; 486 -1.4; 535 -1.1; 588 -0.8; 647 -0.6; 712 -0.3; 783 0.0; 861 0.2; 947 0.1; 1042 -0.1; 1146 -0.5; 1261 -0.7; 1387 -0.8; 1526 -0.7; 1678 -0.3; 1846 0.2; 2031 0.5; 2234 0.7; 2457 1.1; 2703 1.8; 2973 2.4; 3270 1.6; 3597 1.1; 3957 2.7; 4353 3.1; 4788 2.8; 5267 4.0; 5793 5.8; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.8; 9330 -2.1; 10263 -2.8; 11289 -5.5; 12418 -5.3; 13660 -0.9; 15026 0.0; 16529 -1.4; 18182 -2.4; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony IER-M7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-59**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony IER-M7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 35 Hz    | 0.37 | -1.1 dB |
| Peaking | 162 Hz   | 0.49 | -3.4 dB |
| Peaking | 3908 Hz  | 1.16 | 2.1 dB  |
| Peaking | 6032 Hz  | 3.5  | 5.7 dB  |
| Peaking | 11538 Hz | 2.32 | -6.2 dB |
| Peaking | 862 Hz   | 2.88 | 0.8 dB  |
| Peaking | 1384 Hz  | 2.69 | -1.0 dB |
| Peaking | 2824 Hz  | 7.87 | 1.1 dB  |
| Peaking | 17718 Hz | 4.49 | -2.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Sony%20IER-M7/Sony%20IER-M7.png)