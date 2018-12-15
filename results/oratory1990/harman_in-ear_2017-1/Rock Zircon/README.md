# Rock Zircon

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 5.8; 45 5.3; 49 4.7; 54 4.0; 60 3.1; 66 2.2; 72 1.4; 79 0.4; 87 -0.6; 96 -1.6; 106 -2.5; 116 -3.4; 128 -4.1; 141 -4.6; 155 -4.9; 170 -4.1; 187 -6.1; 206 -6.6; 227 -6.2; 249 -5.7; 274 -5.0; 302 -4.1; 332 -3.1; 365 -2.3; 402 -1.6; 442 -0.9; 486 -0.3; 535 0.2; 588 0.6; 647 0.9; 712 1.0; 783 1.1; 861 0.9; 947 0.4; 1042 -0.3; 1146 -1.1; 1261 -1.8; 1387 -2.3; 1526 -2.7; 1678 -3.1; 1846 -3.1; 2031 -2.6; 2234 -2.0; 2457 -2.3; 2703 -2.6; 2973 -3.3; 3270 -3.0; 3597 -2.4; 3957 -2.0; 4353 -2.6; 4788 -4.5; 5267 -8.2; 5793 -11.9; 6373 -9.2; 7010 -7.7; 7711 -8.2; 8482 -6.2; 9330 -2.7; 10263 -0.2; 11289 0.0; 12418 -4.9; 13660 -17.5; 15026 -27.3; 16529 -29.6; 18182 -26.0; 20000 -17.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Rock Zircon GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Rock Zircon ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 0.7  | 6.9 dB   |
| Peaking | 186 Hz   | 0.95 | -6.7 dB  |
| Peaking | 1831 Hz  | 1.85 | -2.8 dB  |
| Peaking | 5826 Hz  | 4.12 | -9.2 dB  |
| Peaking | 17023 Hz | 1.37 | -32.8 dB |
| Peaking | 698 Hz   | 1.23 | 2.8 dB   |
| Peaking | 1305 Hz  | 0.15 | -0.9 dB  |
| Peaking | 7772 Hz  | 3.11 | -5.6 dB  |
| Peaking | 11601 Hz | 1.41 | 16.9 dB  |
| Peaking | 14549 Hz | 1.63 | -16.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Rock%20Zircon/Rock%20Zircon.png)