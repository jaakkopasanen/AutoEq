# B&O PLAY Earset Wireless

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.8dB
GraphicEQ: 21 0.0; 23 4.2; 25 2.6; 28 0.5; 31 -1.4; 34 -3.1; 37 -4.7; 41 -6.5; 45 -8.1; 49 -9.4; 54 -10.8; 60 -12.0; 66 -12.9; 72 -13.3; 79 -13.5; 87 -13.4; 96 -13.0; 106 -12.3; 116 -11.6; 128 -10.6; 141 -9.4; 155 -8.4; 170 -7.6; 187 -7.2; 206 -7.0; 227 -6.9; 249 -6.6; 274 -6.1; 302 -5.5; 332 -4.9; 365 -4.1; 402 -3.5; 442 -2.8; 486 -2.0; 535 -1.4; 588 -0.9; 647 -0.5; 712 -0.3; 783 -0.3; 861 -0.2; 947 -0.0; 1042 -0.0; 1146 -0.3; 1261 -0.9; 1387 -1.9; 1526 -2.9; 1678 -3.4; 1846 -3.3; 2031 -2.5; 2234 -0.6; 2457 1.2; 2703 1.3; 2973 -0.8; 3270 -3.7; 3597 -5.7; 3957 -7.9; 4353 -11.0; 4788 -12.6; 5267 -12.5; 5793 -9.6; 6373 -7.6; 7010 -6.3; 7711 -6.2; 8482 -9.0; 9330 -12.1; 10263 -10.9; 11289 -6.8; 12418 -4.2; 13660 -2.1; 15026 -0.7; 16529 -1.7; 18182 -0.6; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`B&O PLAY Earset Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-68**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `B&O PLAY Earset Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 18 Hz   | 0.59 | 12.9 dB  |
| Peaking | 70 Hz   | 0.42 | -15.8 dB |
| Peaking | 1680 Hz | 5.05 | -3.2 dB  |
| Peaking | 4904 Hz | 2.29 | -12.8 dB |
| Peaking | 9691 Hz | 2.13 | -11.5 dB |
| Peaking | 171 Hz  | 1.65 | 2.4 dB   |
| Peaking | 251 Hz  | 0.62 | -2.3 dB  |
| Peaking | 666 Hz  | 0.77 | 1.8 dB   |
| Peaking | 2580 Hz | 1.12 | -3.2 dB  |
| Peaking | 2632 Hz | 3.16 | 6.7 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/B&O%20PLAY%20Earset%20Wireless/B&O%20PLAY%20Earset%20Wireless.png)