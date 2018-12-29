# Apple iPod Ear Buds sample A
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 6.0; 116 6.0; 128 6.0; 141 5.9; 155 4.5; 170 3.0; 187 1.8; 206 0.5; 227 -0.4; 249 -1.1; 274 -1.5; 302 -1.7; 332 -1.7; 365 -1.5; 402 -1.1; 442 -0.2; 486 0.0; 535 0.3; 588 0.4; 647 0.1; 712 -0.1; 783 -0.0; 861 -0.1; 947 -0.0; 1042 0.0; 1146 0.0; 1261 -0.0; 1387 -0.4; 1526 -0.8; 1678 -1.1; 1846 -0.8; 2031 0.3; 2234 1.4; 2457 0.2; 2703 -2.9; 2973 -5.2; 3270 -3.8; 3597 -0.7; 3957 0.4; 4353 -0.5; 4788 -0.4; 5267 0.7; 5793 -2.7; 6373 -6.7; 7010 -4.2; 7711 -2.8; 8482 -4.3; 9330 -2.6; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Apple iPod Ear Buds sample A GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Apple iPod Ear Buds sample A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 62 Hz   |  0.2  | 6.6 dB  |
| Peaking | 222 Hz  |  2.82 | -2.6 dB |
| Peaking | 317 Hz  |  1.33 | -4.7 dB |
| Peaking | 3014 Hz |  6.18 | -5.7 dB |
| Peaking | 6725 Hz |  3.1  | -5.9 dB |
| Peaking | 18 Hz   |  1.97 | 1.2 dB  |
| Peaking | 137 Hz  |  6.58 | 1.3 dB  |
| Peaking | 3911 Hz |  8.25 | 1.3 dB  |
| Peaking | 5345 Hz | 11.1  | 2.8 dB  |
| Peaking | 8766 Hz |  8.66 | -3.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Apple%20iPod%20Ear%20Buds%20sample%20A/Apple%20iPod%20Ear%20Buds%20sample%20A.png)