# Shure SE215

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.1dB
GraphicEQ: 21 -3.1; 23 -3.2; 25 -3.4; 28 -3.5; 31 -3.7; 34 -3.8; 37 -3.9; 41 -4.0; 45 -4.2; 49 -4.3; 54 -4.5; 60 -4.7; 66 -4.9; 72 -5.2; 79 -5.4; 87 -5.7; 96 -6.0; 106 -6.2; 116 -6.4; 128 -6.5; 141 -6.5; 155 -6.5; 170 -6.3; 187 -6.2; 206 -5.9; 227 -5.6; 249 -5.2; 274 -4.8; 302 -4.4; 332 -4.0; 365 -3.5; 402 -3.0; 442 -2.5; 486 -2.1; 535 -1.6; 588 -1.1; 647 -0.7; 712 -0.2; 783 0.1; 861 0.3; 947 0.2; 1042 -0.2; 1146 -0.8; 1261 -1.1; 1387 -1.2; 1526 -1.6; 1678 -1.9; 1846 -2.2; 2031 -2.8; 2234 -3.3; 2457 -2.8; 2703 -1.3; 2973 0.2; 3270 1.2; 3597 1.3; 3957 0.5; 4353 -1.7; 4788 -5.1; 5267 -3.7; 5793 1.0; 6373 3.7; 7010 2.5; 7711 0.1; 8482 -2.0; 9330 -0.2; 10263 0.0; 11289 -0.1; 12418 -1.0; 13660 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE215 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-40**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE215 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 53 Hz    | 0.27 | -3.6 dB  |
| Peaking | 180 Hz   | 0.62 | -4.3 dB  |
| Peaking | 2155 Hz  | 2.44 | -3.7 dB  |
| Peaking | 4938 Hz  | 4.31 | -11.8 dB |
| Peaking | 5161 Hz  | 1.55 | 5.9 dB   |
| Peaking | 821 Hz   | 3.62 | 1.2 dB   |
| Peaking | 6587 Hz  | 7.16 | 3.1 dB   |
| Peaking | 8438 Hz  | 5.28 | -2.6 dB  |
| Peaking | 10054 Hz | 2.89 | 1.7 dB   |
| Peaking | 10175 Hz | 1.43 | -1.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Shure%20SE215/Shure%20SE215.png)