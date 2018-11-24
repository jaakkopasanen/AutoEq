# Sony MDR-1R

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.7; 34 5.1; 37 4.4; 41 3.6; 45 3.0; 49 2.4; 54 1.8; 60 1.2; 66 0.7; 72 0.1; 79 -0.6; 87 -1.1; 96 -1.4; 106 -1.7; 116 -1.7; 128 -1.0; 141 -0.7; 155 -1.5; 170 -0.3; 187 -0.4; 206 -1.1; 227 -1.3; 249 -0.7; 274 -0.5; 302 0.6; 332 1.6; 365 2.9; 402 3.6; 442 4.0; 486 3.7; 535 3.4; 588 3.2; 647 2.5; 712 1.9; 783 1.9; 861 1.1; 947 0.5; 1042 -0.2; 1146 -0.7; 1261 -1.2; 1387 -2.2; 1526 -3.1; 1678 -3.5; 1846 -3.0; 2031 -2.1; 2234 -0.4; 2457 2.1; 2703 4.1; 2973 5.9; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-1R GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-1R ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 27 Hz   |  0.66 | 7.3 dB  |
| Peaking | 120 Hz  |  0.26 | -2.6 dB |
| Peaking | 469 Hz  |  1.12 | 5.4 dB  |
| Peaking | 1758 Hz |  1.64 | -6.3 dB |
| Peaking | 3750 Hz |  0.88 | 7.6 dB  |
| Peaking | 179 Hz  | 10.97 | 1.6 dB  |
| Peaking | 2974 Hz |  4.86 | 1.8 dB  |
| Peaking | 3665 Hz |  1.8  | -1.2 dB |
| Peaking | 6187 Hz |  2.34 | 5.4 dB  |
| Peaking | 7490 Hz |  1.52 | -4.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-1R/Sony%20MDR-1R.png)