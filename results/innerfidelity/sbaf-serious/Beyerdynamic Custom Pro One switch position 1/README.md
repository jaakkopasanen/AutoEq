# Beyerdynamic Custom Pro One switch position 1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 5.9; 41 5.5; 45 5.1; 49 5.0; 54 5.0; 60 4.8; 66 5.1; 72 5.9; 79 6.0; 87 6.0; 96 3.3; 106 -2.6; 116 -4.0; 128 -5.4; 141 -5.9; 155 -5.3; 170 -5.3; 187 -6.5; 206 -6.1; 227 -5.7; 249 -5.2; 274 -4.8; 302 -4.3; 332 -3.9; 365 -3.4; 402 -3.0; 442 -2.4; 486 -2.2; 535 -1.9; 588 -1.3; 647 -1.1; 712 -1.1; 783 0.1; 861 0.1; 947 -0.1; 1042 0.1; 1146 0.2; 1261 0.1; 1387 -0.5; 1526 -1.5; 1678 -2.4; 1846 -3.1; 2031 -3.5; 2234 -3.2; 2457 -1.7; 2703 -0.5; 2973 1.1; 3270 1.9; 3597 2.7; 3957 3.8; 4353 5.3; 4788 5.9; 5267 6.0; 5793 6.0; 6373 4.6; 7010 2.5; 7711 0.3; 8482 -0.0; 9330 -1.2; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic Custom Pro One switch position 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic Custom Pro One switch position 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 40 Hz   | 0.41 | 8.6 dB   |
| Peaking | 84 Hz   | 2.21 | 10.0 dB  |
| Peaking | 125 Hz  | 0.55 | -11.1 dB |
| Peaking | 2056 Hz | 2.82 | -4.3 dB  |
| Peaking | 4995 Hz | 1.72 | 6.8 dB   |
| Peaking | 162 Hz  | 6.71 | 2.5 dB   |
| Peaking | 170 Hz  | 0.9  | -0.7 dB  |
| Peaking | 928 Hz  | 2.01 | 1.0 dB   |
| Peaking | 6452 Hz | 4.72 | 2.2 dB   |
| Peaking | 8410 Hz | 1.95 | -2.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20Custom%20Pro%20One%20switch%20position%201/Beyerdynamic%20Custom%20Pro%20One%20switch%20position%201.png)