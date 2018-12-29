# Audio Technica ATH-M50x (Dekoni Sheepskin Earpads)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -0.2; 23 -0.9; 25 -1.6; 28 -2.5; 31 -3.2; 34 -3.7; 37 -4.1; 41 -4.5; 45 -4.8; 49 -4.9; 54 -5.1; 60 -5.2; 66 -5.3; 72 -5.3; 79 -5.2; 87 -5.1; 96 -5.0; 106 -5.1; 116 -5.2; 128 -5.0; 141 -5.3; 155 -5.7; 170 -5.9; 187 -5.9; 206 -5.6; 227 -5.0; 249 -3.9; 274 -2.3; 302 -0.3; 332 0.6; 365 0.5; 402 -0.4; 442 -1.4; 486 -2.1; 535 -2.4; 588 -2.2; 647 -2.1; 712 -1.9; 783 -1.4; 861 -0.8; 947 -0.3; 1042 0.3; 1146 1.1; 1261 1.7; 1387 1.8; 1526 2.5; 1678 2.9; 1846 2.9; 2031 2.6; 2234 1.8; 2457 0.8; 2703 0.7; 2973 1.2; 3270 3.3; 3597 5.8; 3957 3.2; 4353 -0.4; 4788 4.1; 5267 6.0; 5793 1.0; 6373 -1.2; 7010 -2.4; 7711 0.2; 8482 0.0; 9330 -0.6; 10263 -0.2; 11289 -0.5; 12418 -4.7; 13660 -9.4; 15026 -9.9; 16529 -6.9; 18182 -5.0; 20000 -9.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-M50x (Dekoni Sheepskin Earpads) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-M50x (Dekoni Sheepskin Earpads) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 73 Hz    | 0.45 | -5.3 dB  |
| Peaking | 189 Hz   | 2.19 | -3.7 dB  |
| Peaking | 1679 Hz  | 2.72 | 2.8 dB   |
| Peaking | 4187 Hz  | 1.24 | 3.7 dB   |
| Peaking | 15349 Hz | 1.25 | -10.2 dB |
| Peaking | 343 Hz   | 4.03 | 2.9 dB   |
| Peaking | 579 Hz   | 1.85 | -2.2 dB  |
| Peaking | 5277 Hz  | 6.38 | 8.1 dB   |
| Peaking | 5688 Hz  | 2.09 | -4.2 dB  |
| Peaking | 10711 Hz | 3.88 | 3.1 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Audio%20Technica%20ATH-M50x%20(Dekoni%20Sheepskin%20Earpads)/Audio%20Technica%20ATH-M50x%20(Dekoni%20Sheepskin%20Earpads).png)