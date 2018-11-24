# 1More Triple Driver In-Ear

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 0.9; 25 0.5; 28 0.1; 31 -0.3; 34 -0.6; 37 -0.8; 41 -1.1; 45 -1.3; 49 -1.5; 54 -1.7; 60 -2.0; 66 -2.3; 72 -2.5; 79 -2.7; 87 -2.9; 96 -3.3; 106 -3.8; 116 -4.2; 128 -4.7; 141 -4.9; 155 -4.9; 170 -4.9; 187 -4.8; 206 -4.7; 227 -4.7; 249 -4.5; 274 -3.9; 302 -3.1; 332 -2.4; 365 -1.7; 402 -1.1; 442 -0.3; 486 0.5; 535 1.3; 588 1.9; 647 2.4; 712 2.3; 783 1.7; 861 1.0; 947 0.3; 1042 -0.1; 1146 -0.2; 1261 -0.4; 1387 -1.0; 1526 -1.8; 1678 -2.4; 1846 -2.7; 2031 -3.1; 2234 -3.1; 2457 -2.5; 2703 -1.4; 2973 -0.1; 3270 0.8; 3597 0.1; 3957 -2.8; 4353 -6.2; 4788 -3.3; 5267 3.9; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -1.2; 9330 -1.5; 10263 -0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -2.8; 16529 -4.5; 18182 -5.2; 20000 -9.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`1More Triple Driver In-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1More Triple Driver In-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 175 Hz   | 0.54 | -5.2 dB |
| Peaking | 620 Hz   | 1.42 | 3.7 dB  |
| Peaking | 1974 Hz  | 2.01 | -3.4 dB |
| Peaking | 4464 Hz  | 5.84 | -8.4 dB |
| Peaking | 5805 Hz  | 3.55 | 7.7 dB  |
| Peaking | 21 Hz    | 2    | 1.5 dB  |
| Peaking | 2488 Hz  | 5.75 | -0.8 dB |
| Peaking | 3275 Hz  | 5.03 | 1.9 dB  |
| Peaking | 13144 Hz | 2.51 | 2.6 dB  |
| Peaking | 21217 Hz | 0.39 | -9.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/1More%20Triple%20Driver%20In-Ear/1More%20Triple%20Driver%20In-Ear.png)