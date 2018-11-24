# AKG K712 (Dekoni Sheepskin Earpads)

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.4; 25 1.0; 28 0.6; 31 0.3; 34 0.0; 37 -0.2; 41 -0.4; 45 -0.6; 49 -0.8; 54 -1.0; 60 -1.2; 66 -1.4; 72 -1.6; 79 -1.8; 87 -2.1; 96 -2.4; 106 -2.7; 116 -3.1; 128 -3.6; 141 -4.1; 155 -4.4; 170 -4.7; 187 -4.8; 206 -5.0; 227 -5.0; 249 -5.0; 274 -4.8; 302 -4.4; 332 -3.9; 365 -3.3; 402 -2.8; 442 -2.3; 486 -1.8; 535 -1.0; 588 -0.2; 647 0.6; 712 0.5; 783 0.1; 861 -0.1; 947 -0.1; 1042 0.2; 1146 0.9; 1261 1.6; 1387 1.4; 1526 0.3; 1678 -1.2; 1846 -2.4; 2031 -3.9; 2234 -4.9; 2457 -4.6; 2703 -2.4; 2973 1.8; 3270 5.8; 3597 6.0; 3957 6.0; 4353 5.4; 4788 2.3; 5267 -2.1; 5793 -3.3; 6373 -0.5; 7010 -1.8; 7711 -2.3; 8482 -0.2; 9330 0.0; 10263 0.0; 11289 -1.0; 12418 -2.6; 13660 -0.9; 15026 -1.3; 16529 -5.0; 18182 -8.3; 20000 -8.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K712 (Dekoni Sheepskin Earpads) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K712 (Dekoni Sheepskin Earpads) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 215 Hz   | 0.63 | -5.3 dB  |
| Peaking | 2355 Hz  | 1.56 | -13.4 dB |
| Peaking | 3905 Hz  | 0.72 | 20.4 dB  |
| Peaking | 5450 Hz  | 0.94 | -14.7 dB |
| Peaking | 19064 Hz | 0.96 | -9.5 dB  |
| Peaking | 20 Hz    | 1.92 | 1.8 dB   |
| Peaking | 662 Hz   | 2.68 | 2.1 dB   |
| Peaking | 840 Hz   | 0.98 | -1.4 dB  |
| Peaking | 1305 Hz  | 4.51 | 1.7 dB   |
| Peaking | 23999 Hz | 1.82 | 0.4 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/AKG%20K712%20(Dekoni%20Sheepskin%20Earpads)/AKG%20K712%20(Dekoni%20Sheepskin%20Earpads).png)