# B&O PLAY H9

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.6dB
GraphicEQ: 21 -13.9; 23 -13.7; 25 -13.4; 28 -13.0; 31 -12.5; 34 -11.9; 37 -11.3; 41 -10.5; 45 -9.9; 49 -9.3; 54 -8.8; 60 -8.5; 66 -8.3; 72 -8.1; 79 -7.9; 87 -7.7; 96 -7.5; 106 -7.3; 116 -7.1; 128 -7.0; 141 -6.9; 155 -6.7; 170 -6.5; 187 -6.1; 206 -5.6; 227 -4.9; 249 -4.3; 274 -3.6; 302 -3.1; 332 -2.5; 365 -1.7; 402 -1.1; 442 -0.4; 486 0.2; 535 0.6; 588 1.0; 647 1.4; 712 1.7; 783 1.8; 861 1.5; 947 0.5; 1042 -0.3; 1146 -0.9; 1261 -1.5; 1387 -2.2; 1526 -2.8; 1678 -3.3; 1846 -3.6; 2031 -5.0; 2234 -6.3; 2457 -7.1; 2703 -5.7; 2973 -6.0; 3270 -8.9; 3597 -9.8; 3957 -7.4; 4353 -5.1; 4788 -4.0; 5267 -2.9; 5793 2.6; 6373 4.3; 7010 2.5; 7711 -0.1; 8482 -5.7; 9330 -9.6; 10263 -11.5; 11289 -12.6; 12418 -12.0; 13660 -9.2; 15026 -5.7; 16529 -4.7; 18182 -5.4; 20000 -2.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`B&O PLAY H9 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-45**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `B&O PLAY H9 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 14 Hz    | 0.22 | -14.3 dB |
| Peaking | 163 Hz   | 1.05 | -4.4 dB  |
| Peaking | 2289 Hz  | 2.21 | -5.9 dB  |
| Peaking | 3560 Hz  | 3.81 | -9.0 dB  |
| Peaking | 11927 Hz | 1.62 | -13.9 dB |
| Peaking | 706 Hz   | 2.35 | 2.6 dB   |
| Peaking | 5127 Hz  | 2.05 | -6.6 dB  |
| Peaking | 6312 Hz  | 2.1  | 11.3 dB  |
| Peaking | 9368 Hz  | 3.75 | -5.5 dB  |
| Peaking | 18396 Hz | 1.87 | -4.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/B&O%20PLAY%20H9/B&O%20PLAY%20H9.png)