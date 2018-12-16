# Rock Zircon

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.0dB
GraphicEQ: 21 -1.3; 23 -1.5; 25 -1.8; 28 -2.1; 31 -2.3; 34 -2.6; 37 -2.8; 41 -3.0; 45 -3.3; 49 -3.5; 54 -3.8; 60 -4.2; 66 -4.5; 72 -4.9; 79 -5.3; 87 -5.7; 96 -6.1; 106 -6.5; 116 -6.8; 128 -6.9; 141 -6.9; 155 -6.6; 170 -5.3; 187 -6.7; 206 -6.8; 227 -6.1; 249 -5.4; 274 -4.6; 302 -3.8; 332 -2.9; 365 -2.3; 402 -1.6; 442 -1.0; 486 -0.4; 535 0.1; 588 0.4; 647 0.7; 712 0.9; 783 0.9; 861 0.8; 947 0.4; 1042 -0.3; 1146 -1.2; 1261 -2.1; 1387 -2.9; 1526 -3.6; 1678 -4.1; 1846 -4.1; 2031 -3.9; 2234 -4.0; 2457 -4.8; 2703 -5.5; 2973 -6.4; 3270 -6.0; 3597 -5.2; 3957 -4.5; 4353 -4.6; 4788 -6.2; 5267 -9.9; 5793 -13.8; 6373 -11.5; 7010 -10.9; 7711 -12.0; 8482 -8.8; 9330 -2.5; 10263 0.0; 11289 0.0; 12418 -3.2; 13660 -9.5; 15026 -11.8; 16529 -11.6; 18182 -10.3; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Rock Zircon GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-10**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Rock Zircon ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 101 Hz   | 0.64 | -6.2 dB  |
| Peaking | 219 Hz   | 1.82 | -3.8 dB  |
| Peaking | 2541 Hz  | 1.11 | -4.6 dB  |
| Peaking | 6297 Hz  | 1.94 | -12.2 dB |
| Peaking | 16882 Hz | 1.17 | -12.9 dB |
| Peaking | 761 Hz   | 1.64 | 2.0 dB   |
| Peaking | 1487 Hz  | 3.22 | -1.9 dB  |
| Peaking | 8121 Hz  | 4.7  | -7.2 dB  |
| Peaking | 10839 Hz | 1.45 | 6.4 dB   |
| Peaking | 13861 Hz | 2.99 | -6.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Rock%20Zircon/Rock%20Zircon.png)