# Sony MDR-V600
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 5.9; 45 5.2; 49 4.2; 54 3.2; 60 2.3; 66 1.8; 72 1.3; 79 0.1; 87 -0.8; 96 -1.1; 106 -0.5; 116 -0.1; 128 -1.3; 141 -2.4; 155 -3.1; 170 -2.7; 187 -2.7; 206 -3.5; 227 -3.8; 249 -3.9; 274 -3.8; 302 -3.5; 332 -3.3; 365 -3.0; 402 -3.2; 442 -3.6; 486 -2.9; 535 -2.6; 588 -2.1; 647 -0.7; 712 -1.4; 783 -1.0; 861 -0.8; 947 -0.5; 1042 0.4; 1146 1.1; 1261 2.0; 1387 2.1; 1526 1.4; 1678 0.9; 1846 1.5; 2031 3.0; 2234 4.4; 2457 5.4; 2703 6.0; 2973 6.0; 3270 6.0; 3597 4.5; 3957 4.0; 4353 2.1; 4788 3.8; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -1.9; 10263 -0.2; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-V600 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-V600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 0.75 | 6.8 dB  |
| Peaking | 226 Hz  | 0.63 | -3.8 dB |
| Peaking | 465 Hz  | 2.35 | -1.5 dB |
| Peaking | 2826 Hz | 1.44 | 6.2 dB  |
| Peaking | 5764 Hz | 3.51 | 5.8 dB  |
| Peaking | 91 Hz   | 4.25 | -1.3 dB |
| Peaking | 114 Hz  | 6.74 | 1.4 dB  |
| Peaking | 1309 Hz | 4.53 | 1.8 dB  |
| Peaking | 1732 Hz | 5.4  | -1.1 dB |
| Peaking | 9330 Hz | 5.42 | -2.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-V600/Sony%20MDR-V600.png)