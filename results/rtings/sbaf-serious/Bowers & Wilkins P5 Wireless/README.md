# Bowers & Wilkins P5 Wireless

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.6dB
GraphicEQ: 21 -3.2; 23 -3.4; 25 -3.5; 28 -3.7; 31 -3.9; 34 -3.8; 37 -3.7; 41 -3.6; 45 -3.6; 49 -3.6; 54 -3.6; 60 -3.5; 66 -3.4; 72 -3.2; 79 -3.0; 87 -2.8; 96 -2.7; 106 -2.7; 116 -2.5; 128 -2.4; 141 -2.2; 155 -2.0; 170 -1.9; 187 -1.9; 206 -1.7; 227 -1.6; 249 -1.4; 274 -1.0; 302 -0.4; 332 0.3; 365 1.5; 402 2.5; 442 3.2; 486 3.6; 535 3.7; 588 3.7; 647 3.5; 712 3.0; 783 2.2; 861 1.3; 947 0.5; 1042 -0.3; 1146 -0.7; 1261 -1.2; 1387 -2.6; 1526 -4.1; 1678 -4.7; 1846 -3.4; 2031 -0.5; 2234 1.4; 2457 1.9; 2703 2.7; 2973 3.5; 3270 4.1; 3597 4.5; 3957 2.5; 4353 0.1; 4788 0.5; 5267 2.8; 5793 3.9; 6373 3.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -1.3; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bowers & Wilkins P5 Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-45**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers & Wilkins P5 Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.4dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 23 Hz    |  0.08 | -3.4 dB |
| Peaking | 535 Hz   |  1.25 | 4.9 dB  |
| Peaking | 1621 Hz  |  2.68 | -5.8 dB |
| Peaking | 3104 Hz  |  1.96 | 4.5 dB  |
| Peaking | 6156 Hz  |  3.97 | 3.9 dB  |
| Peaking | 2217 Hz  | 11.26 | 1.1 dB  |
| Peaking | 4501 Hz  |  5.37 | -4.3 dB |
| Peaking | 4522 Hz  |  2.31 | 2.2 dB  |
| Peaking | 8326 Hz  |  3.75 | -0.8 dB |
| Peaking | 17942 Hz |  4.23 | -1.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Bowers%20&%20Wilkins%20P5%20Wireless/Bowers%20&%20Wilkins%20P5%20Wireless.png)