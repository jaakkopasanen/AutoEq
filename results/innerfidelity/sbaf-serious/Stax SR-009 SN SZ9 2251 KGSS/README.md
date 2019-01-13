# Stax SR-009 SN SZ9 2251 KGSS
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 5.5; 66 5.5; 72 4.7; 79 4.4; 87 4.4; 96 4.2; 106 4.1; 116 4.0; 128 3.7; 141 3.5; 155 3.3; 170 3.1; 187 3.1; 206 2.9; 227 3.0; 249 2.8; 274 2.8; 302 2.8; 332 2.7; 365 2.5; 402 2.4; 442 2.4; 486 2.0; 535 1.8; 588 1.8; 647 1.5; 712 1.0; 783 1.0; 861 0.9; 947 0.3; 1042 0.0; 1146 -0.4; 1261 -0.5; 1387 -0.6; 1526 -0.6; 1678 -1.0; 1846 1.3; 2031 3.1; 2234 3.9; 2457 4.8; 2703 3.0; 2973 3.3; 3270 3.2; 3597 3.7; 3957 2.5; 4353 0.8; 4788 -0.5; 5267 0.7; 5793 5.8; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-009 SN SZ9 2251 KGSS GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-009 SN SZ9 2251 KGSS ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 114 Hz   |  0.09 | 8.3 dB  |
| Peaking | 533 Hz   |  0.1  | -5.3 dB |
| Peaking | 2372 Hz  |  2.39 | 6.8 dB  |
| Peaking | 3541 Hz  |  3.28 | 5.0 dB  |
| Peaking | 6164 Hz  |  4    | 7.8 dB  |
| Peaking | 53 Hz    |  3.47 | 0.4 dB  |
| Peaking | 1645 Hz  |  9.96 | -1.4 dB |
| Peaking | 4060 Hz  |  0.13 | 0.2 dB  |
| Peaking | 4991 Hz  | 11.4  | -1.9 dB |
| Peaking | 11293 Hz |  2.68 | 0.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-009%20SN%20SZ9%202251%20KGSS/Stax%20SR-009%20SN%20SZ9%202251%20KGSS.png)