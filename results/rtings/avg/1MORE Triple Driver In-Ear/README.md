# 1MORE Triple Driver In-Ear

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.8dB
GraphicEQ: 21 0.0; 23 0.5; 25 0.3; 28 -0.1; 31 -0.3; 34 -0.5; 37 -0.7; 41 -0.9; 45 -1.0; 49 -1.1; 54 -1.3; 60 -1.8; 66 -2.1; 72 -2.5; 79 -2.8; 87 -3.3; 96 -3.8; 106 -4.3; 116 -4.8; 128 -5.2; 141 -5.5; 155 -5.6; 170 -5.5; 187 -5.4; 206 -5.2; 227 -5.2; 249 -5.0; 274 -4.5; 302 -4.0; 332 -3.4; 365 -2.8; 402 -2.1; 442 -1.4; 486 -0.7; 535 0.1; 588 0.8; 647 1.3; 712 1.4; 783 1.3; 861 0.9; 947 0.3; 1042 -0.2; 1146 -0.4; 1261 -0.7; 1387 -1.0; 1526 -1.4; 1678 -2.0; 1846 -2.8; 2031 -3.6; 2234 -3.5; 2457 -3.0; 2703 -2.3; 2973 -1.6; 3270 -1.8; 3597 -3.0; 3957 -5.2; 4353 -7.5; 4788 -4.9; 5267 0.9; 5793 3.4; 6373 3.6; 7010 2.4; 7711 0.3; 8482 -0.7; 9330 -0.3; 10263 -0.6; 11289 -2.6; 12418 -4.2; 13660 -5.9; 15026 -8.7; 16529 -10.9; 18182 -12.8; 20000 -17.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`1MORE Triple Driver In-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-38**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1MORE Triple Driver In-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 135 Hz  | 0.9  | -5.1 dB |
| Peaking | 257 Hz  | 1.84 | -3.1 dB |
| Peaking | 2112 Hz | 2.5  | -3.6 dB |
| Peaking | 4404 Hz | 3.14 | -8.4 dB |
| Peaking | 5886 Hz | 3.56 | 6.3 dB  |
| Peaking | 20 Hz   | 1.8  | 1.0 dB  |
| Peaking | 379 Hz  | 3.05 | -0.9 dB |
| Peaking | 607 Hz  | 3.38 | 0.8 dB  |
| Peaking | 741 Hz  | 2.13 | 1.7 dB  |
| Peaking | 1404 Hz | 1.68 | -0.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/1MORE%20Triple%20Driver%20In-Ear/1MORE%20Triple%20Driver%20In-Ear.png)