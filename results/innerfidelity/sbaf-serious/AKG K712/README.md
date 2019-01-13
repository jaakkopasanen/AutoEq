# AKG K712
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.5dB
GraphicEQ: 21 0.0; 23 4.5; 25 4.0; 28 3.3; 31 2.8; 34 2.3; 37 1.9; 41 1.4; 45 1.1; 49 0.7; 54 0.4; 60 -0.1; 66 -0.4; 72 -0.8; 79 -1.2; 87 -1.7; 96 -2.1; 106 -2.5; 116 -2.6; 128 -2.9; 141 -2.9; 155 -3.2; 170 -3.4; 187 -3.0; 206 -3.1; 227 -3.3; 249 -3.4; 274 -3.3; 302 -3.1; 332 -2.7; 365 -2.5; 402 -2.3; 442 -2.0; 486 -1.8; 535 -1.1; 588 -0.6; 647 -0.4; 712 -0.3; 783 -0.1; 861 -0.2; 947 0.1; 1042 -0.0; 1146 0.4; 1261 0.4; 1387 -0.5; 1526 -1.7; 1678 -2.9; 1846 -4.3; 2031 -4.9; 2234 -4.3; 2457 -2.2; 2703 1.0; 2973 2.7; 3270 2.7; 3597 1.4; 3957 -1.0; 4353 -3.0; 4788 -2.1; 5267 -0.0; 5793 -0.1; 6373 -1.9; 7010 -3.7; 7711 -4.8; 8482 -5.7; 9330 -3.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -1.2; 18182 -6.0; 20000 -3.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K712 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-55**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K712 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 16 Hz    | 0.71 | 5.8 dB  |
| Peaking | 183 Hz   | 0.55 | -3.6 dB |
| Peaking | 1989 Hz  | 4.15 | -5.5 dB |
| Peaking | 8074 Hz  | 3.3  | -6.0 dB |
| Peaking | 18638 Hz | 2.4  | -7.0 dB |
| Peaking | 1000 Hz  | 2.16 | 0.7 dB  |
| Peaking | 2352 Hz  | 5.13 | -2.8 dB |
| Peaking | 3091 Hz  | 2.61 | 4.1 dB  |
| Peaking | 4352 Hz  | 5.33 | -3.8 dB |
| Peaking | 12912 Hz | 1.45 | 0.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K712/AKG%20K712.png)