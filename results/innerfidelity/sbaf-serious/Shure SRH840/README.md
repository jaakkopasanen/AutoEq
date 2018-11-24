# Shure SRH840

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 5.8; 31 5.0; 34 3.9; 37 3.0; 41 1.8; 45 0.9; 49 0.1; 54 -0.9; 60 -1.7; 66 -2.2; 72 -2.5; 79 -2.6; 87 -2.8; 96 -3.1; 106 -3.5; 116 -3.6; 128 -4.0; 141 -4.2; 155 -4.0; 170 -3.0; 187 -3.6; 206 -3.5; 227 -3.2; 249 -3.0; 274 -2.8; 302 -4.4; 332 -4.0; 365 -3.4; 402 -3.0; 442 -2.5; 486 -2.3; 535 -1.9; 588 -1.2; 647 -0.8; 712 -0.6; 783 -0.2; 861 -0.2; 947 0.2; 1042 -0.1; 1146 -0.4; 1261 -0.8; 1387 -1.5; 1526 -2.6; 1678 -3.3; 1846 -4.0; 2031 -4.5; 2234 -5.2; 2457 -4.8; 2703 -3.8; 2973 -3.0; 3270 -2.2; 3597 -1.3; 3957 -0.3; 4353 -0.3; 4788 -1.3; 5267 1.5; 5793 5.5; 6373 5.5; 7010 2.5; 7711 0.1; 8482 -5.3; 9330 -6.9; 10263 -2.2; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH840 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH840 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 26 Hz    |  0.96 | 7.3 dB  |
| Peaking | 136 Hz   |  0.34 | -4.2 dB |
| Peaking | 2279 Hz  |  1.67 | -5.3 dB |
| Peaking | 6212 Hz  |  3.9  | 7.2 dB  |
| Peaking | 9060 Hz  |  4.66 | -8.3 dB |
| Peaking | 340 Hz   |  4.06 | -1.5 dB |
| Peaking | 958 Hz   |  1.56 | 1.2 dB  |
| Peaking | 1621 Hz  |  4.04 | -1.0 dB |
| Peaking | 4790 Hz  | 11.5  | -2.0 dB |
| Peaking | 11124 Hz |  7.57 | 1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SRH840/Shure%20SRH840.png)