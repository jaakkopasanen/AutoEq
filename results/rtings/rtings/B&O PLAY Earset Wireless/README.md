# B&O PLAY Earset Wireless

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.4dB
GraphicEQ: 21 0.0; 23 3.8; 25 2.4; 28 0.4; 31 -1.4; 34 -3.1; 37 -4.6; 41 -6.3; 45 -7.8; 49 -9.1; 54 -10.5; 60 -11.8; 66 -12.7; 72 -13.3; 79 -13.7; 87 -13.7; 96 -13.4; 106 -12.8; 116 -12.1; 128 -11.1; 141 -10.0; 155 -9.0; 170 -8.3; 187 -7.7; 206 -7.5; 227 -7.4; 249 -7.1; 274 -6.8; 302 -6.3; 332 -5.8; 365 -5.1; 402 -4.5; 442 -3.9; 486 -3.2; 535 -2.6; 588 -2.0; 647 -1.5; 712 -1.1; 783 -0.8; 861 -0.4; 947 -0.1; 1042 -0.1; 1146 -0.5; 1261 -1.2; 1387 -1.9; 1526 -2.5; 1678 -3.1; 1846 -3.3; 2031 -2.9; 2234 -1.1; 2457 0.8; 2703 0.7; 2973 -1.9; 3270 -5.6; 3597 -7.8; 3957 -9.1; 4353 -11.0; 4788 -12.4; 5267 -12.9; 5793 -11.0; 6373 -10.2; 7010 -8.8; 7711 -7.4; 8482 -9.4; 9330 -13.6; 10263 -14.3; 11289 -11.3; 12418 -8.7; 13660 -5.9; 15026 -4.0; 16529 -5.1; 18182 -3.4; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`B&O PLAY Earset Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-63**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `B&O PLAY Earset Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 14 Hz    | 0.29 | 15.3 dB  |
| Peaking | 61 Hz    | 0.23 | -11.4 dB |
| Peaking | 69 Hz    | 0.76 | -8.0 dB  |
| Peaking | 4858 Hz  | 1.82 | -11.2 dB |
| Peaking | 10386 Hz | 1.22 | -12.8 dB |
| Peaking | 1886 Hz  | 2.83 | -3.7 dB  |
| Peaking | 2675 Hz  | 2.09 | 5.3 dB   |
| Peaking | 3411 Hz  | 3.3  | -4.1 dB  |
| Peaking | 7928 Hz  | 9.71 | 2.3 dB   |
| Peaking | 17133 Hz | 3.86 | -3.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/B&O%20PLAY%20Earset%20Wireless/B&O%20PLAY%20Earset%20Wireless.png)