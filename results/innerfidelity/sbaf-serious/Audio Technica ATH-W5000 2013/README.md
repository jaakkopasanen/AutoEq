# Audio Technica ATH-W5000 2013

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 5.6; 60 4.3; 66 3.4; 72 3.2; 79 2.4; 87 1.0; 96 0.2; 106 -0.2; 116 -0.2; 128 -0.5; 141 -0.5; 155 -0.5; 170 -0.2; 187 -0.2; 206 -0.2; 227 -0.0; 249 0.0; 274 -0.0; 302 0.2; 332 0.9; 365 1.4; 402 2.2; 442 4.0; 486 5.0; 535 5.3; 588 5.0; 647 3.7; 712 2.7; 783 2.3; 861 1.3; 947 0.5; 1042 -0.3; 1146 -0.9; 1261 -1.2; 1387 -1.6; 1526 -2.0; 1678 -1.0; 1846 -0.6; 2031 -1.3; 2234 -0.6; 2457 2.6; 2703 5.7; 2973 6.0; 3270 6.0; 3597 6.0; 3957 3.5; 4353 1.7; 4788 0.8; 5267 4.4; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -1.8; 10263 -1.0; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-W5000 2013 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-W5000 2013 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 38 Hz    |  0.45 | 8.9 dB  |
| Peaking | 516 Hz   |  0.06 | -4.4 dB |
| Peaking | 540 Hz   |  0.91 | 9.1 dB  |
| Peaking | 3125 Hz  |  1.89 | 10.1 dB |
| Peaking | 6006 Hz  |  3.08 | 8.0 dB  |
| Peaking | 102 Hz   |  4.6  | -0.9 dB |
| Peaking | 194 Hz   |  2.85 | 0.9 dB  |
| Peaking | 2138 Hz  | 12.46 | -1.7 dB |
| Peaking | 3724 Hz  | 16.56 | 2.2 dB  |
| Peaking | 13009 Hz |  2.87 | 0.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-W5000%202013/Audio%20Technica%20ATH-W5000%202013.png)