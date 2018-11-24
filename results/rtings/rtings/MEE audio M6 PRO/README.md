# MEE audio M6 PRO

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.1dB
GraphicEQ: 21 0.0; 23 1.6; 25 1.4; 28 1.2; 31 1.0; 34 0.8; 37 0.7; 41 0.6; 45 0.6; 49 0.5; 54 0.3; 60 -0.2; 66 -0.5; 72 -0.8; 79 -1.2; 87 -1.6; 96 -2.0; 106 -2.6; 116 -3.0; 128 -3.4; 141 -3.7; 155 -3.9; 170 -3.9; 187 -3.9; 206 -3.7; 227 -3.5; 249 -3.3; 274 -2.9; 302 -2.5; 332 -1.9; 365 -1.4; 402 -1.0; 442 -0.7; 486 -0.3; 535 0.3; 588 0.8; 647 1.1; 712 1.3; 783 1.4; 861 1.0; 947 0.3; 1042 -0.3; 1146 -1.4; 1261 -1.9; 1387 -2.3; 1526 -2.9; 1678 -3.7; 1846 -4.6; 2031 -5.5; 2234 -6.1; 2457 -6.8; 2703 -8.3; 2973 -8.5; 3270 -7.4; 3597 -6.7; 3957 -7.1; 4353 -9.5; 4788 -12.1; 5267 -12.7; 5793 -6.2; 6373 -3.5; 7010 -2.1; 7711 -3.0; 8482 -4.8; 9330 -4.0; 10263 -0.3; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MEE audio M6 PRO GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-21**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MEE audio M6 PRO ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 15 Hz    | 0.53 | 2.1 dB   |
| Peaking | 166 Hz   | 0.94 | -4.3 dB  |
| Peaking | 2686 Hz  | 1.31 | -7.3 dB  |
| Peaking | 4990 Hz  | 2.86 | -11.4 dB |
| Peaking | 23998 Hz | 2.16 | -2.7 dB  |
| Peaking | 294 Hz   | 2.48 | -0.9 dB  |
| Peaking | 765 Hz   | 1.48 | 2.4 dB   |
| Peaking | 1360 Hz  | 1.56 | -1.1 dB  |
| Peaking | 6504 Hz  | 3.87 | 1.5 dB   |
| Peaking | 8723 Hz  | 5.44 | -4.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/MEE%20audio%20M6%20PRO/MEE%20audio%20M6%20PRO.png)