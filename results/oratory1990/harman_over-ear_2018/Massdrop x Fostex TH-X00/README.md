# Massdrop x Fostex TH-X00

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.3dB
GraphicEQ: 21 0.0; 23 4.3; 25 3.3; 28 2.3; 31 1.7; 34 1.3; 37 1.1; 41 1.0; 45 1.0; 49 0.9; 54 0.9; 60 1.0; 66 1.0; 72 0.9; 79 0.8; 87 0.6; 96 0.5; 106 0.2; 116 -0.0; 128 -0.2; 141 -0.3; 155 -0.4; 170 -0.4; 187 -0.4; 206 -0.4; 227 -0.3; 249 -0.2; 274 0.0; 302 0.3; 332 0.6; 365 0.9; 402 1.3; 442 1.7; 486 2.1; 535 2.7; 588 3.1; 647 2.0; 712 0.2; 783 0.8; 861 1.3; 947 0.2; 1042 0.0; 1146 0.2; 1261 0.1; 1387 -0.1; 1526 -0.1; 1678 0.1; 1846 0.4; 2031 0.8; 2234 0.9; 2457 1.0; 2703 1.8; 2973 5.9; 3270 6.0; 3597 6.0; 3957 5.9; 4353 3.2; 4788 0.1; 5267 -1.1; 5793 -0.1; 6373 4.3; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 -0.7; 11289 -4.2; 12418 -6.9; 13660 -6.1; 15026 -2.7; 16529 -1.3; 18182 -2.8; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x Fostex TH-X00 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-63**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x Fostex TH-X00 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 14 Hz    |  1.18 | 8.9 dB  |
| Peaking | 546 Hz   |  2.55 | 3.0 dB  |
| Peaking | 3447 Hz  |  2.72 | 7.1 dB  |
| Peaking | 6595 Hz  |  8.22 | 4.9 dB  |
| Peaking | 12975 Hz |  2.25 | -7.5 dB |
| Peaking | 73 Hz    |  1.75 | 0.7 dB  |
| Peaking | 168 Hz   |  1.56 | -0.7 dB |
| Peaking | 4118 Hz  | 10.02 | 2.3 dB  |
| Peaking | 5261 Hz  |  5.51 | -2.6 dB |
| Peaking | 9681 Hz  |  5.42 | 1.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Massdrop%20x%20Fostex%20TH-X00/Massdrop%20x%20Fostex%20TH-X00.png)