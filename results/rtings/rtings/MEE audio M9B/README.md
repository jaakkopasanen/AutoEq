# MEE audio M9B

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.6dB
GraphicEQ: 21 -13.8; 23 -13.4; 25 -12.8; 28 -11.6; 31 -10.6; 34 -9.8; 37 -9.2; 41 -8.8; 45 -8.7; 49 -8.7; 54 -8.7; 60 -8.5; 66 -8.3; 72 -7.9; 79 -7.3; 87 -6.8; 96 -6.4; 106 -6.1; 116 -6.0; 128 -5.9; 141 -5.8; 155 -5.6; 170 -5.3; 187 -5.0; 206 -4.5; 227 -4.0; 249 -3.5; 274 -3.1; 302 -2.7; 332 -2.2; 365 -1.6; 402 -1.0; 442 -0.4; 486 0.1; 535 0.7; 588 1.2; 647 1.5; 712 1.4; 783 1.3; 861 0.7; 947 0.1; 1042 0.0; 1146 -0.0; 1261 -0.1; 1387 -0.1; 1526 0.1; 1678 0.1; 1846 0.1; 2031 0.2; 2234 0.7; 2457 0.9; 2703 -0.8; 2973 -3.4; 3270 -6.1; 3597 -7.1; 3957 -6.1; 4353 -5.2; 4788 -3.9; 5267 -3.5; 5793 -6.3; 6373 -13.0; 7010 -10.8; 7711 -4.2; 8482 -2.5; 9330 -8.7; 10263 -12.8; 11289 -6.7; 12418 -0.1; 13660 -0.3; 15026 -5.5; 16529 -7.3; 18182 -5.8; 20000 -8.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MEE audio M9B GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-15**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MEE audio M9B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.1dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 168 Hz   |  1.07 | -3.1 dB  |
| Peaking | 6341 Hz  |  1.7  | -9.8 dB  |
| Peaking | 10233 Hz |  6.38 | -11.4 dB |
| Peaking | 18625 Hz |  0.95 | -7.4 dB  |
| Peaking | 21 Hz    |  1    | -12.0 dB |
| Peaking | 61 Hz    |  0.6  | -6.1 dB  |
| Peaking | 3548 Hz  |  4.31 | -5.8 dB  |
| Peaking | 5135 Hz  |  9.66 | 3.1 dB   |
| Peaking | 5590 Hz  | 12.58 | 3.3 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/MEE%20audio%20M9B/MEE%20audio%20M9B.png)