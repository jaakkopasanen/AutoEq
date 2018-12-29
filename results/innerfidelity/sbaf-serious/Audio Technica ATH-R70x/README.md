# Audio Technica ATH-R70x
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.8dB
GraphicEQ: 21 0.0; 23 5.3; 25 4.5; 28 3.5; 31 2.7; 34 1.9; 37 1.3; 41 0.6; 45 0.0; 49 -0.4; 54 -0.9; 60 -1.4; 66 -1.7; 72 -2.0; 79 -2.3; 87 -2.4; 96 -2.1; 106 -2.7; 116 -3.0; 128 -3.2; 141 -3.2; 155 -3.3; 170 -3.2; 187 -3.2; 206 -3.1; 227 -2.8; 249 -2.7; 274 -2.5; 302 -2.2; 332 -2.0; 365 -1.8; 402 -1.5; 442 -1.2; 486 -1.2; 535 -1.1; 588 -0.7; 647 -0.6; 712 -0.8; 783 -0.3; 861 -0.5; 947 -0.4; 1042 -0.2; 1146 -0.4; 1261 -0.8; 1387 -1.5; 1526 -2.1; 1678 -2.7; 1846 -2.6; 2031 -2.1; 2234 -1.4; 2457 -0.3; 2703 1.6; 2973 2.2; 3270 1.3; 3597 -0.7; 3957 0.8; 4353 2.1; 4788 3.6; 5267 5.6; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.0; 9330 -1.3; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -0.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-R70x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-67**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-R70x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 20 Hz   |  1.12 | 6.7 dB  |
| Peaking | 145 Hz  |  0.46 | -3.4 dB |
| Peaking | 1808 Hz |  2.15 | -2.9 dB |
| Peaking | 2858 Hz |  6.91 | 3.2 dB  |
| Peaking | 5682 Hz |  2.94 | 6.8 dB  |
| Peaking | 1032 Hz |  4.71 | 0.5 dB  |
| Peaking | 3626 Hz | 13.31 | -1.6 dB |
| Peaking | 6553 Hz | 10.53 | 1.8 dB  |
| Peaking | 8895 Hz |  3.13 | -1.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-R70x/Audio%20Technica%20ATH-R70x.png)