# Bowers & Wilkins P5 Series 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.1dB
GraphicEQ: 21 -3.1; 23 -3.4; 25 -3.7; 28 -4.1; 31 -4.4; 34 -4.5; 37 -4.5; 41 -4.5; 45 -4.5; 49 -4.5; 54 -4.6; 60 -4.6; 66 -4.7; 72 -4.8; 79 -4.8; 87 -4.8; 96 -4.7; 106 -4.6; 116 -4.4; 128 -4.1; 141 -3.6; 155 -3.2; 170 -2.7; 187 -2.3; 206 -1.7; 227 -1.0; 249 -0.3; 274 0.5; 302 1.5; 332 2.6; 365 3.7; 402 3.9; 442 3.3; 486 2.5; 535 2.0; 588 1.7; 647 1.4; 712 1.2; 783 1.0; 861 0.7; 947 0.3; 1042 -0.3; 1146 -1.0; 1261 -1.8; 1387 -2.9; 1526 -4.1; 1678 -5.2; 1846 -6.3; 2031 -6.7; 2234 -6.4; 2457 -5.7; 2703 -4.4; 2973 -1.6; 3270 -0.1; 3597 -0.6; 3957 -1.2; 4353 -1.0; 4788 0.6; 5267 1.2; 5793 -0.2; 6373 -1.6; 7010 0.9; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.6; 20000 -2.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bowers & Wilkins P5 Series 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-40**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers & Wilkins P5 Series 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 0.88 | -2.2 dB |
| Peaking | 105 Hz   | 0.35 | -4.8 dB |
| Peaking | 387 Hz   | 0.92 | 5.5 dB  |
| Peaking | 2060 Hz  | 1.52 | -7.4 dB |
| Peaking | 3245 Hz  | 5.25 | 2.3 dB  |
| Peaking | 380 Hz   | 5.09 | 1.1 dB  |
| Peaking | 757 Hz   | 0.75 | -1.7 dB |
| Peaking | 853 Hz   | 1.35 | 2.2 dB  |
| Peaking | 5118 Hz  | 7.63 | 2.0 dB  |
| Peaking | 19896 Hz | 1.79 | -2.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bowers%20&%20Wilkins%20P5%20Series%202/Bowers%20&%20Wilkins%20P5%20Series%202.png)