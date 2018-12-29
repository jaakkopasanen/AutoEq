# Sol Republic Tracks
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -0.4; 23 -1.1; 25 -1.8; 28 -2.5; 31 -3.1; 34 -3.5; 37 -3.9; 41 -4.3; 45 -4.5; 49 -4.7; 54 -4.9; 60 -4.9; 66 -4.9; 72 -5.0; 79 -5.1; 87 -5.0; 96 -4.6; 106 -4.7; 116 -4.8; 128 -5.0; 141 -5.1; 155 -5.1; 170 -4.6; 187 -4.8; 206 -4.5; 227 -3.7; 249 -2.6; 274 -0.9; 302 1.2; 332 3.2; 365 5.6; 402 6.0; 442 6.0; 486 6.0; 535 5.2; 588 3.6; 647 2.1; 712 0.8; 783 0.2; 861 -0.1; 947 -0.0; 1042 -0.1; 1146 0.6; 1261 1.2; 1387 1.5; 1526 2.7; 1678 2.4; 1846 1.5; 2031 2.3; 2234 3.4; 2457 4.9; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 5.3; 4788 4.0; 5267 4.5; 5793 5.9; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sol Republic Tracks GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sol Republic Tracks ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 151 Hz  | 0.23 | -6.2 dB |
| Peaking | 425 Hz  | 1.33 | 11.4 dB |
| Peaking | 2711 Hz | 1.25 | 4.1 dB  |
| Peaking | 3856 Hz | 1.75 | 3.8 dB  |
| Peaking | 6041 Hz | 4.59 | 4.9 dB  |
| Peaking | 19 Hz   | 2.19 | 1.5 dB  |
| Peaking | 214 Hz  | 5.08 | -1.1 dB |
| Peaking | 1601 Hz | 5.43 | 3.0 dB  |
| Peaking | 1780 Hz | 3.98 | -1.9 dB |
| Peaking | 8377 Hz | 3.89 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sol%20Republic%20Tracks/Sol%20Republic%20Tracks.png)