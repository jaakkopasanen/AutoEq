# Massdrop x Fostex T-X0

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 5.5; 87 4.3; 96 3.2; 106 1.8; 116 0.6; 128 -0.5; 141 -1.5; 155 -2.5; 170 -3.3; 187 -3.8; 206 -4.2; 227 -4.3; 249 -4.3; 274 -4.2; 302 -3.4; 332 -1.4; 365 -0.5; 402 0.3; 442 1.1; 486 2.0; 535 2.8; 588 4.9; 647 5.5; 712 4.8; 783 1.9; 861 0.8; 947 0.3; 1042 -0.3; 1146 0.4; 1261 1.7; 1387 2.6; 1526 3.5; 1678 4.8; 1846 5.5; 2031 6.0; 2234 5.8; 2457 4.4; 2703 3.5; 2973 3.3; 3270 2.8; 3597 2.6; 3957 3.9; 4353 4.2; 4788 2.5; 5267 1.4; 5793 0.3; 6373 3.2; 7010 2.5; 7711 -0.7; 8482 -0.3; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.4; 20000 -3.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x Fostex T-X0 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x Fostex T-X0 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 53 Hz   |  0.28 | 7.4 dB  |
| Peaking | 192 Hz  |  0.83 | -8.3 dB |
| Peaking | 615 Hz  |  2.65 | 6.2 dB  |
| Peaking | 2019 Hz |  1.91 | 6.0 dB  |
| Peaking | 4199 Hz |  1.97 | 3.2 dB  |
| Peaking | 19 Hz   |  2.35 | 0.7 dB  |
| Peaking | 293 Hz  |  3.59 | -2.6 dB |
| Peaking | 327 Hz  |  1.79 | 1.8 dB  |
| Peaking | 1021 Hz |  4.84 | -1.7 dB |
| Peaking | 6648 Hz | 11.87 | 3.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Massdrop%20x%20Fostex%20T-X0/Massdrop%20x%20Fostex%20T-X0.png)