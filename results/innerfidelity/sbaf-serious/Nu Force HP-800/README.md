# Nu Force HP-800

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.8dB
GraphicEQ: 21 -2.1; 23 -2.9; 25 -3.5; 28 -4.3; 31 -4.9; 34 -5.3; 37 -5.6; 41 -6.0; 45 -6.2; 49 -6.5; 54 -6.5; 60 -6.4; 66 -6.5; 72 -6.8; 79 -7.2; 87 -7.4; 96 -7.5; 106 -7.8; 116 -7.8; 128 -7.9; 141 -8.0; 155 -7.9; 170 -7.5; 187 -7.6; 206 -7.3; 227 -7.0; 249 -6.7; 274 -5.9; 302 -5.0; 332 -3.9; 365 -1.9; 402 -0.3; 442 -0.6; 486 -0.5; 535 -0.4; 588 -1.5; 647 -1.9; 712 -1.6; 783 -0.9; 861 -0.5; 947 -0.2; 1042 0.2; 1146 0.5; 1261 0.4; 1387 -0.3; 1526 -1.3; 1678 -2.4; 1846 -3.5; 2031 -4.3; 2234 -5.3; 2457 -6.4; 2703 -6.8; 2973 -5.9; 3270 -4.5; 3597 -3.0; 3957 -1.5; 4353 -0.2; 4788 2.7; 5267 5.4; 5793 4.1; 6373 2.5; 7010 -0.9; 7711 0.0; 8482 0.0; 9330 -0.5; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Nu Force HP-800 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-58**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Nu Force HP-800 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 54 Hz   |  0.5  | -5.8 dB |
| Peaking | 144 Hz  |  1.03 | -5.1 dB |
| Peaking | 248 Hz  |  2.18 | -3.9 dB |
| Peaking | 2658 Hz |  1.71 | -7.2 dB |
| Peaking | 5383 Hz |  3.91 | 6.8 dB  |
| Peaking | 415 Hz  |  6.67 | 1.9 dB  |
| Peaking | 673 Hz  |  4.68 | -1.5 dB |
| Peaking | 1228 Hz |  2.26 | 1.6 dB  |
| Peaking | 1803 Hz |  3.78 | -1.1 dB |
| Peaking | 7173 Hz | 12.3  | -1.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Nu%20Force%20HP-800/Nu%20Force%20HP-800.png)