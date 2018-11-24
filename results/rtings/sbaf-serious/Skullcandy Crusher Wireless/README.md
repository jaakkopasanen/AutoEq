# Skullcandy Crusher Wireless

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.9dB
GraphicEQ: 21 -11.7; 23 -11.4; 25 -11.2; 28 -10.7; 31 -10.2; 34 -9.6; 37 -9.0; 41 -8.2; 45 -7.4; 49 -7.6; 54 -9.4; 60 -8.3; 66 -7.5; 72 -7.9; 79 -8.5; 87 -9.1; 96 -9.5; 106 -9.7; 116 -9.5; 128 -9.3; 141 -9.0; 155 -8.3; 170 -7.5; 187 -6.7; 206 -5.7; 227 -4.6; 249 -3.7; 274 -3.1; 302 -2.4; 332 -1.6; 365 -0.8; 402 -0.2; 442 0.1; 486 0.2; 535 0.4; 588 0.6; 647 1.0; 712 0.9; 783 -0.5; 861 -0.6; 947 -0.2; 1042 0.2; 1146 0.8; 1261 1.3; 1387 1.4; 1526 1.2; 1678 0.9; 1846 0.8; 2031 0.7; 2234 0.8; 2457 1.0; 2703 0.4; 2973 -0.4; 3270 -0.5; 3597 0.4; 3957 1.0; 4353 0.4; 4788 1.0; 5267 1.8; 5793 1.1; 6373 -0.6; 7010 -2.3; 7711 -3.1; 8482 -4.7; 9330 -6.2; 10263 -4.4; 11289 -1.7; 12418 -2.0; 13660 -1.9; 15026 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Crusher Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-19**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Crusher Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.0dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 10 Hz   | 0.95 | -11.8 dB |
| Peaking | 20 Hz   | 0.27 | -7.6 dB  |
| Peaking | 131 Hz  | 0.78 | -8.1 dB  |
| Peaking | 1214 Hz | 0.11 | 1.0 dB   |
| Peaking | 9223 Hz | 2.15 | -6.7 dB  |
| Peaking | 793 Hz  | 1.19 | 2.1 dB   |
| Peaking | 858 Hz  | 2.52 | -3.4 dB  |
| Peaking | 3128 Hz | 5.78 | -1.8 dB  |
| Peaking | 5453 Hz | 4.03 | 1.8 dB   |
| Peaking | 6955 Hz | 6.11 | -1.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Skullcandy%20Crusher%20Wireless/Skullcandy%20Crusher%20Wireless.png)