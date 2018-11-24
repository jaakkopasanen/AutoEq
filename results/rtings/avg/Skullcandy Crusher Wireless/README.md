# Skullcandy Crusher Wireless

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.7dB
GraphicEQ: 21 -12.1; 23 -11.8; 25 -11.4; 28 -10.9; 31 -10.3; 34 -9.6; 37 -8.9; 41 -8.0; 45 -7.1; 49 -7.3; 54 -9.0; 60 -8.0; 66 -7.3; 72 -7.9; 79 -8.6; 87 -9.4; 96 -10.0; 106 -10.1; 116 -10.0; 128 -9.8; 141 -9.5; 155 -8.9; 170 -8.1; 187 -7.3; 206 -6.2; 227 -5.1; 249 -4.3; 274 -3.8; 302 -3.2; 332 -2.5; 365 -1.9; 402 -1.2; 442 -1.0; 486 -1.0; 535 -0.8; 588 -0.5; 647 -0.1; 712 0.1; 783 -0.9; 861 -0.8; 947 -0.2; 1042 0.2; 1146 0.6; 1261 1.1; 1387 1.5; 1526 1.5; 1678 1.3; 1846 0.8; 2031 0.3; 2234 0.4; 2457 0.5; 2703 -0.4; 2973 -2.0; 3270 -3.1; 3597 -2.7; 3957 -1.4; 4353 -0.9; 4788 -0.6; 5267 -1.2; 5793 -2.8; 6373 -4.4; 7010 -5.4; 7711 -4.6; 8482 -4.2; 9330 -5.1; 10263 -5.6; 11289 -7.0; 12418 -9.8; 13660 -8.9; 15026 -5.3; 16529 -3.8; 18182 -1.4; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Crusher Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-16**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Crusher Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 12 Hz    | 1.07 | -12.2 dB |
| Peaking | 21 Hz    | 0.39 | -7.6 dB  |
| Peaking | 126 Hz   | 0.79 | -8.8 dB  |
| Peaking | 6968 Hz  | 2.26 | -3.8 dB  |
| Peaking | 12864 Hz | 1.39 | -9.6 dB  |
| Peaking | 428 Hz   | 4.43 | 0.5 dB   |
| Peaking | 1487 Hz  | 2.39 | 1.9 dB   |
| Peaking | 2435 Hz  | 4.48 | 1.1 dB   |
| Peaking | 3273 Hz  | 3.57 | -3.1 dB  |
| Peaking | 4867 Hz  | 5.32 | 1.3 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Skullcandy%20Crusher%20Wireless/Skullcandy%20Crusher%20Wireless.png)