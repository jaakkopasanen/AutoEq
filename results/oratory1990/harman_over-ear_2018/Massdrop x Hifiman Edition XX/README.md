# Massdrop x Hifiman Edition XX
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.7; 25 2.7; 28 2.7; 31 2.7; 34 2.7; 37 2.9; 41 2.9; 45 2.3; 49 1.7; 54 1.7; 60 1.7; 66 1.2; 72 1.0; 79 0.9; 87 0.7; 96 0.3; 106 -0.1; 116 -0.3; 128 -0.7; 141 -1.0; 155 -1.4; 170 -1.6; 187 -2.1; 206 -2.5; 227 -2.5; 249 -2.6; 274 -1.4; 302 0.2; 332 -0.6; 365 -1.1; 402 -1.6; 442 -2.3; 486 -2.4; 535 -0.5; 588 1.6; 647 0.4; 712 -0.3; 783 -0.2; 861 2.0; 947 0.8; 1042 -0.3; 1146 4.2; 1261 4.8; 1387 5.3; 1526 6.0; 1678 6.0; 1846 6.0; 2031 6.0; 2234 4.7; 2457 2.6; 2703 1.2; 2973 0.5; 3270 0.8; 3597 1.8; 3957 2.2; 4353 2.1; 4788 -0.1; 5267 2.0; 5793 1.4; 6373 1.6; 7010 2.1; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x Hifiman Edition XX GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x Hifiman Edition XX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.18 | 3.1 dB  |
| Peaking | 186 Hz  | 0.49 | -3.4 dB |
| Peaking | 1035 Hz | 9.21 | -3.1 dB |
| Peaking | 1600 Hz | 1.23 | 6.7 dB  |
| Peaking | 6134 Hz | 2.43 | 1.5 dB  |
| Peaking | 310 Hz  | 6.67 | 2.3 dB  |
| Peaking | 522 Hz  | 2.5  | -2.7 dB |
| Peaking | 571 Hz  | 6.14 | 4.2 dB  |
| Peaking | 2964 Hz | 5.42 | -1.7 dB |
| Peaking | 3935 Hz | 5.93 | 1.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Massdrop%20x%20Hifiman%20Edition%20XX/Massdrop%20x%20Hifiman%20Edition%20XX.png)