# Polk Audio UltraFocus 8000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.0dB
GraphicEQ: 21 -7.1; 23 -6.5; 25 -5.9; 28 -5.2; 31 -4.7; 34 -4.2; 37 -3.8; 41 -3.4; 45 -3.2; 49 -3.0; 54 -2.7; 60 -2.5; 66 -2.4; 72 -2.3; 79 -2.1; 87 -2.0; 96 -1.9; 106 -2.0; 116 -2.0; 128 -2.0; 141 -1.9; 155 -1.8; 170 -1.9; 187 -1.9; 206 -1.9; 227 -1.8; 249 -1.8; 274 -1.6; 302 -1.4; 332 -1.0; 365 -0.9; 402 -0.9; 442 -0.7; 486 -0.6; 535 -0.5; 588 -0.5; 647 -0.2; 712 -0.3; 783 -0.2; 861 -0.2; 947 0.1; 1042 -0.1; 1146 -0.0; 1261 -0.1; 1387 -0.3; 1526 -0.8; 1678 -1.3; 1846 -1.6; 2031 -1.4; 2234 -0.7; 2457 0.5; 2703 1.5; 2973 1.9; 3270 1.3; 3597 0.3; 3957 -1.7; 4353 -2.0; 4788 -1.4; 5267 1.1; 5793 3.4; 6373 4.8; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -0.9; 10263 -2.0; 11289 -0.4; 12418 0.0; 13660 -0.2; 15026 -0.3; 16529 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio UltraFocus 8000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-49**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio UltraFocus 8000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 17 Hz   | 0.79 | -6.8 dB |
| Peaking | 52 Hz   | 0.3  | -1.5 dB |
| Peaking | 224 Hz  | 0.85 | -1.2 dB |
| Peaking | 6346 Hz | 2.98 | 8.7 dB  |
| Peaking | 6389 Hz | 1.11 | -3.6 dB |
| Peaking | 2008 Hz | 2.12 | -3.0 dB |
| Peaking | 2935 Hz | 1.28 | 3.4 dB  |
| Peaking | 4193 Hz | 3.66 | -3.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Polk%20Audio%20UltraFocus%208000/Polk%20Audio%20UltraFocus%208000.png)