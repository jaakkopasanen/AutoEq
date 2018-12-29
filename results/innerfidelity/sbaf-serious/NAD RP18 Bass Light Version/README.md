# NAD RP18 Bass Light Version
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 6.0; 116 6.0; 128 6.0; 141 6.0; 155 6.0; 170 6.0; 187 6.0; 206 6.0; 227 6.0; 249 5.4; 274 4.2; 302 3.4; 332 2.3; 365 2.1; 402 1.6; 442 1.0; 486 0.4; 535 1.0; 588 0.9; 647 0.2; 712 -0.2; 783 -0.1; 861 -0.6; 947 -0.1; 1042 0.2; 1146 0.5; 1261 0.2; 1387 0.1; 1526 -0.2; 1678 -0.8; 1846 -0.0; 2031 0.4; 2234 0.2; 2457 -0.7; 2703 -0.1; 2973 1.3; 3270 1.7; 3597 3.2; 3957 2.4; 4353 1.2; 4788 -0.4; 5267 5.2; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NAD RP18 Bass Light Version GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NAD RP18 Bass Light Version ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 46 Hz   |  0.13 | 6.1 dB  |
| Peaking | 217 Hz  |  1.33 | 2.7 dB  |
| Peaking | 415 Hz  |  0.52 | -1.8 dB |
| Peaking | 3621 Hz |  5.47 | 3.2 dB  |
| Peaking | 5939 Hz |  4.06 | 6.8 dB  |
| Peaking | 1152 Hz |  8.72 | 0.7 dB  |
| Peaking | 2553 Hz | 15.55 | -1.6 dB |
| Peaking | 4780 Hz |  9.81 | -2.7 dB |
| Peaking | 5276 Hz | 11.84 | 2.5 dB  |
| Peaking | 8223 Hz |  5.31 | -0.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NAD%20RP18%20Bass%20Light%20Version/NAD%20RP18%20Bass%20Light%20Version.png)