# V-MODA Crossfade II Wireless

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -0.0; 23 -0.4; 25 -0.7; 28 -1.2; 31 -1.7; 34 -2.0; 37 -2.2; 41 -2.4; 45 -2.7; 49 -2.9; 54 -3.2; 60 -3.4; 66 -3.6; 72 -3.7; 79 -3.8; 87 -3.9; 96 -4.1; 106 -4.3; 116 -4.5; 128 -4.5; 141 -4.4; 155 -4.3; 170 -4.0; 187 -3.6; 206 -3.0; 227 -2.3; 249 -1.5; 274 0.4; 302 1.4; 332 1.9; 365 2.8; 402 3.3; 442 3.1; 486 3.1; 535 3.1; 588 2.7; 647 2.5; 712 1.9; 783 1.2; 861 0.6; 947 0.1; 1042 0.0; 1146 0.2; 1261 0.5; 1387 0.7; 1526 0.8; 1678 1.1; 1846 1.7; 2031 2.1; 2234 2.2; 2457 1.7; 2703 2.1; 2973 1.9; 3270 2.2; 3597 1.6; 3957 1.8; 4353 4.1; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`V-MODA Crossfade II Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-MODA Crossfade II Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 59 Hz   |  0.69 | -2.3 dB |
| Peaking | 164 Hz  |  0.69 | -4.6 dB |
| Peaking | 402 Hz  |  1.02 | 5.0 dB  |
| Peaking | 2263 Hz |  2    | 1.8 dB  |
| Peaking | 5359 Hz |  2.21 | 6.7 dB  |
| Peaking | 652 Hz  |  4.14 | 0.7 dB  |
| Peaking | 985 Hz  |  3.64 | -0.9 dB |
| Peaking | 4599 Hz | 10.84 | 2.0 dB  |
| Peaking | 6490 Hz |  4.61 | 4.5 dB  |
| Peaking | 6761 Hz |  1.74 | -2.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/V-MODA%20Crossfade%20II%20Wireless/V-MODA%20Crossfade%20II%20Wireless.png)