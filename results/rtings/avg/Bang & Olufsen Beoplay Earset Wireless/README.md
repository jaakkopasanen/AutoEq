# Bang & Olufsen Beoplay Earset Wireless

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.4dB
GraphicEQ: 21 0.0; 23 3.8; 25 2.4; 28 0.4; 31 -1.4; 34 -3.1; 37 -4.6; 41 -6.3; 45 -7.8; 49 -9.1; 54 -10.5; 60 -11.8; 66 -12.7; 72 -13.3; 79 -13.7; 87 -13.7; 96 -13.4; 106 -12.8; 116 -12.1; 128 -11.1; 141 -10.0; 155 -9.0; 170 -8.3; 187 -7.7; 206 -7.5; 227 -7.4; 249 -7.1; 274 -6.8; 302 -6.3; 332 -5.8; 365 -5.1; 402 -4.5; 442 -3.9; 486 -3.2; 535 -2.6; 588 -2.0; 647 -1.5; 712 -1.1; 783 -0.8; 861 -0.4; 947 -0.1; 1042 -0.1; 1146 -0.5; 1261 -1.2; 1387 -1.9; 1526 -2.5; 1678 -3.1; 1846 -3.3; 2031 -2.9; 2234 -1.1; 2457 0.8; 2703 0.5; 2973 -2.4; 3270 -6.3; 3597 -8.8; 3957 -10.3; 4353 -12.3; 4788 -14.2; 5267 -15.5; 5793 -13.5; 6373 -11.4; 7010 -9.5; 7711 -7.8; 8482 -8.5; 9330 -11.0; 10263 -12.0; 11289 -12.1; 12418 -12.0; 13660 -9.2; 15026 -6.6; 16529 -8.1; 18182 -7.8; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bang & Olufsen Beoplay Earset Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-63**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bang & Olufsen Beoplay Earset Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--1.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 76 Hz    | 1.01 | -10.7 dB |
| Peaking | 172 Hz   | 0.48 | -6.4 dB  |
| Peaking | 5036 Hz  | 1.69 | -14.2 dB |
| Peaking | 11441 Hz | 1.14 | -11.2 dB |
| Peaking | 17590 Hz | 2.11 | -6.9 dB  |
| Peaking | 19 Hz    | 1.45 | 7.9 dB   |
| Peaking | 46 Hz    | 2.12 | -2.4 dB  |
| Peaking | 1932 Hz  | 1.9  | -7.3 dB  |
| Peaking | 2607 Hz  | 1.18 | 10.7 dB  |
| Peaking | 3410 Hz  | 1.8  | -7.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bang%20&%20Olufsen%20Beoplay%20Earset%20Wireless/Bang%20&%20Olufsen%20Beoplay%20Earset%20Wireless.png)