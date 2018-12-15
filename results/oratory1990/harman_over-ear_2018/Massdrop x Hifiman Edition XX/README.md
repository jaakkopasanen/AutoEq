# Massdrop x Hifiman Edition XX

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 5.8; 72 5.5; 79 5.1; 87 4.5; 96 3.7; 106 2.8; 116 2.0; 128 1.2; 141 0.4; 155 -0.4; 170 -1.0; 187 -1.8; 206 -2.4; 227 -2.6; 249 -2.6; 274 -1.4; 302 0.2; 332 -0.6; 365 -1.1; 402 -1.6; 442 -2.3; 486 -2.4; 535 -0.5; 588 1.6; 647 0.4; 712 -0.3; 783 -0.2; 861 2.0; 947 0.8; 1042 -0.3; 1146 4.2; 1261 4.8; 1387 5.3; 1526 6.0; 1678 6.0; 1846 6.0; 2031 6.0; 2234 4.7; 2457 2.6; 2703 1.2; 2973 0.5; 3270 0.8; 3597 1.8; 3957 2.2; 4353 2.1; 4788 -0.1; 5267 2.0; 5793 1.4; 6373 1.6; 7010 2.1; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x Hifiman Edition XX GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x Hifiman Edition XX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 41 Hz   | 0.27 | 6.5 dB  |
| Peaking | 194 Hz  | 1.08 | -4.9 dB |
| Peaking | 458 Hz  | 4.94 | -2.8 dB |
| Peaking | 1679 Hz | 1.5  | 6.7 dB  |
| Peaking | 6004 Hz | 2.13 | 1.6 dB  |
| Peaking | 173 Hz  | 3.29 | 0.2 dB  |
| Peaking | 2154 Hz | 4.77 | 1.6 dB  |
| Peaking | 2305 Hz | 3.48 | 0.6 dB  |
| Peaking | 3047 Hz | 1.31 | -2.0 dB |
| Peaking | 3837 Hz | 3.61 | 2.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Massdrop%20x%20Hifiman%20Edition%20XX/Massdrop%20x%20Hifiman%20Edition%20XX.png)