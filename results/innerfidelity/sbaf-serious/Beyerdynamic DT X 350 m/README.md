# Beyerdynamic DT X 350 m
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.1; 25 3.7; 28 3.3; 31 2.9; 34 2.6; 37 2.4; 41 2.3; 45 2.3; 49 1.9; 54 1.2; 60 0.9; 66 0.8; 72 0.9; 79 1.5; 87 1.9; 96 1.0; 106 -0.2; 116 -1.5; 128 -2.5; 141 -2.4; 155 -1.4; 170 0.5; 187 1.4; 206 3.3; 227 5.0; 249 5.3; 274 5.1; 302 4.6; 332 3.6; 365 2.2; 402 1.7; 442 1.5; 486 1.2; 535 0.8; 588 1.0; 647 0.7; 712 0.4; 783 0.4; 861 0.1; 947 0.0; 1042 0.0; 1146 0.2; 1261 0.2; 1387 0.0; 1526 0.0; 1678 -0.4; 1846 -0.6; 2031 -1.3; 2234 -1.0; 2457 -0.2; 2703 0.6; 2973 1.6; 3270 2.9; 3597 5.9; 3957 2.9; 4353 -2.2; 4788 0.4; 5267 3.5; 5793 2.2; 6373 0.3; 7010 -0.6; 7711 -0.3; 8482 -1.2; 9330 -1.2; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -2.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT X 350 m GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT X 350 m ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 138 Hz   |  2.75 | -4.3 dB |
| Peaking | 259 Hz   |  1.58 | 5.7 dB  |
| Peaking | 3591 Hz  |  6.62 | 6.4 dB  |
| Peaking | 24000 Hz |  2.35 | 0.8 dB  |
| Peaking | 17 Hz    |  0.55 | 4.7 dB  |
| Peaking | 88 Hz    |  5.51 | 1.7 dB  |
| Peaking | 4366 Hz  | 10.05 | -3.9 dB |
| Peaking | 5393 Hz  |  6.33 | 3.9 dB  |
| Peaking | 8788 Hz  |  4.64 | -1.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%20X%20350%20m/Beyerdynamic%20DT%20X%20350%20m.png)