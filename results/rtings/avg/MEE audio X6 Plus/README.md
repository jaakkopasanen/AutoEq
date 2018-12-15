# MEE audio X6 Plus

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.8dB
GraphicEQ: 21 -1.8; 23 -1.8; 25 -1.7; 28 -1.2; 31 -0.6; 34 -0.2; 37 0.1; 41 0.3; 45 0.2; 49 0.0; 54 -0.4; 60 -0.8; 66 -0.8; 72 -0.6; 79 -0.4; 87 -0.3; 96 -0.2; 106 -0.3; 116 -0.5; 128 -0.6; 141 -0.9; 155 -0.9; 170 -0.9; 187 -0.8; 206 -0.6; 227 -0.4; 249 -0.2; 274 0.1; 302 0.6; 332 1.0; 365 1.4; 402 1.9; 442 2.2; 486 2.3; 535 2.5; 588 2.7; 647 2.6; 712 2.4; 783 2.0; 861 1.3; 947 0.5; 1042 -0.2; 1146 -0.6; 1261 -0.8; 1387 -1.1; 1526 -1.7; 1678 -2.5; 1846 -3.1; 2031 -3.8; 2234 -4.3; 2457 -5.3; 2703 -6.8; 2973 -7.0; 3270 -5.8; 3597 -5.1; 3957 -5.6; 4353 -7.5; 4788 -10.9; 5267 -12.5; 5793 -6.4; 6373 -2.2; 7010 -0.2; 7711 -0.6; 8482 -1.4; 9330 -0.6; 10263 0.0; 11289 0.0; 12418 -0.7; 13660 -1.1; 15026 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MEE audio X6 Plus GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-28**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MEE audio X6 Plus ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.9dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 175 Hz   |  0.67 | -1.1 dB  |
| Peaking | 554 Hz   |  1.03 | 3.3 dB   |
| Peaking | 2783 Hz  |  1.19 | -6.2 dB  |
| Peaking | 5086 Hz  |  4.3  | -11.7 dB |
| Peaking | 21844 Hz |  1.96 | 0.3 dB   |
| Peaking | 22 Hz    |  0.97 | -1.9 dB  |
| Peaking | 39 Hz    |  2.48 | 1.2 dB   |
| Peaking | 5567 Hz  | 11.89 | -1.7 dB  |
| Peaking | 6901 Hz  |  5.03 | 2.0 dB   |
| Peaking | 13123 Hz |  9.41 | -1.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/MEE%20audio%20X6%20Plus/MEE%20audio%20X6%20Plus.png)